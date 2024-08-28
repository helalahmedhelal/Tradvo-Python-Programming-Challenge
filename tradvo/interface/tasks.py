import subprocess
from celery import shared_task
from django.shortcuts import get_object_or_404
from .models import UploadedApk
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from io import BytesIO
from PIL import Image
import base64
from django.http import JsonResponse
import os


@shared_task
def run_appium_task(request, pk):
    app = get_object_or_404(UploadedApk, pk=pk, uploaded_by=request.user)
    apk_path = app.apk_file_path.path
    
    def get_android_version():
        try:
            result = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.release'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            version = result.stdout.strip()
            return version
        except Exception as e:
            print(f"Error retrieving Android version: {e}")
            return None

    platform_version = get_android_version()

    def get_device_name():
        try:
            # Run the command to list all AVDs
            result = subprocess.run(['emulator', '-list-avds'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Check if the command was successful
            if result.returncode != 0:
                print(f"Error running emulator command: {result.stderr}")
                return None
            
            # Split the output into lines to get AVD names
            avd_names = result.stdout.strip().splitlines()
            
            # Return the first AVD name if the list is not empty
            if avd_names:
                return avd_names[0]
            else:
                print("No AVDs found.")
                return None
    
        except Exception as e:
            print(f"Error retrieving AVD names: {e}")
            return None

    device_name = get_device_name()
    
    def start_emulator():
        try:
            # Start the emulator
            emulator_process = subprocess.Popen(['emulator', '-avd', device_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Give some time for the emulator to start
            time.sleep(30)  # Adjust this time as needed
            
            # Check if emulator is running (this is an example and may need adjustments)
            if emulator_process.poll() is None:
                print("Emulator started successfully.")
            else:
                print("Failed to start the emulator.")
            
        except Exception as e:
            print(f"Error starting the emulator: {e}")
            
        return emulator_process    


    starting_emu=start_emulator()
    
    
    
    if device_name:
        starting_emu
    else: 
            print("No device name available.")
    
    def start_appium_server():
        try:
            # Start the server
            appium_process = subprocess.Popen(['appium'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Wait for the server to start
            time.sleep(5)  # Adjust this time based on how long Appium takes to start on your system

            # Check the logs to see if the server started successfully
            stdout, stderr = appium_process.communicate(timeout=10)
            
            # Look for a successful startup message in the logs
            if "Appium REST http interface listener started" in stdout or "Appium REST http interface listener started" in stderr:
                print("Appium server started successfully.")
            else:
                print("Failed to start the Appium server.")
                print(f"Error output: {stderr}")
            
        except subprocess.TimeoutExpired:
            print("Appium server startup timed out.")
            appium_process.kill()  # Ensure the process is terminated if it exceeds the timeout
        except Exception as e:
            print(f"Error starting the Appium server: {e}")
            
        return appium_process

    
    appium_server_process=start_appium_server()
    
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': platform_version,
        'deviceName': device_name,
        'app': apk_path,
        'automationName': 'UiAutomator2',
        'newCommandTimeout': 300,
        'autoGrantPermissions': True
    }
    url='http://localhost:4723/wd/hub'
    
    try:
        driver = webdriver.Remote(url, desired_caps)
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return JsonResponse({'status': 'error', 'message': 'Failed to initialize WebDriver.'})

    # Check if driver is None
    if driver is None:
        print("Driver initialization failed.")
        return JsonResponse({'status': 'error', 'message': 'Driver initialization failed.'})

    
    def capture_screenshot(filename):
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(BytesIO(screenshot))
        image.save(filename)


    def capture_ui_hierarchy(filename):
        hierarchy = driver.page_source
        with open(filename, 'w') as f:
            f.write(hierarchy)
        
            
    # Start video recording
    driver.start_recording_screen()
    
            
    #Capture initial screen screenshot and UI hierarchy
    initial_screenshot_path = os.path.join('media/screenshots', f'{app.name}_initial.png')
    capture_screenshot(initial_screenshot_path)
    
    
    initial_ui_hierarchy_path = os.path.join('media/ui_hierarchies', f'{app.name}_initial.xml')
    capture_ui_hierarchy(initial_ui_hierarchy_path)
    
    
    # # Simulate a click on the first button
    try:
        first_button=driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[1]')
        
        first_button.click()
        
        time.sleep(5)  # Wait for screen change
    except Exception as e:
        print(f"Error during button click: {e}")
    
    
    # # Capture subsequent screen screenshot and UI hierarchy
    subsequent_screenshot_path = os.path.join('media/screenshots', f'{app.name}_subsequent.png')
    capture_screenshot(subsequent_screenshot_path)
    
    subsequent_ui_hierarchy_path = os.path.join('media/ui_hierarchies', f'{app.name}_subsequent.xml')
    capture_ui_hierarchy(subsequent_ui_hierarchy_path)
    
    # Stop video recording and save
    video_data = driver.stop_recording_screen()
    video_recording_path = os.path.join('media/videos', f'{app.name}_test_video.mp4')
    with open(video_recording_path, 'wb') as f:
        f.write(base64.b64decode(video_data))

    # Determine if the screen has changed
    with open(initial_ui_hierarchy_path, 'r') as f:
        initial_hierarchy = f.read()
    
    with open(subsequent_ui_hierarchy_path, 'r') as f:
        subsequent_hierarchy = f.read()
    
    screen_changed = initial_hierarchy != subsequent_hierarchy

    # Save results to the database
    app.first_screen_screenshot_path = initial_screenshot_path
    app.second_screen_screenshot_path = subsequent_screenshot_path
    app.video_recording_path = video_recording_path
    app.ui_hierarchy = initial_ui_hierarchy_path  # Or save the subsequent one if needed
    app.screen_changed = screen_changed
    app.save()

    driver.quit()
    
    starting_emu.kill()
    
    appium_server_process.kill()
    return ('apk_details')

