from django import forms
from .models import UploadedApk
from django.utils.translation import gettext_lazy as _

class UploadedAppForm(forms.ModelForm):
    class Meta:
        model = UploadedApk
        fields = ['name', 'apk_file_path', 'first_screen_screenshot_path',
                  'second_screen_screenshot_path', 'video_recording_path', 
                  'ui_hierarchy', 'screen_changed']
        
        labels = {
            'name': _('App Name'),
            'apk_file_path': _('APK File'),
            'first_screen_screenshot_path': _('First Screen Screenshot'),
            'second_screen_screenshot_path': _('Second Screen Screenshot'),
            'video_recording_path': _('Video Recording'),
            'ui_hierarchy': _('UI Hierarchy'),
            'screen_changed': _('Screen Changed'),
        }
        
        help_texts = {
            'name': _('Enter the name of the app.'),
            'apk_file_path': _('Upload the APK file.'),
            'first_screen_screenshot_path': _('Upload a screenshot of the first screen.'),
            'second_screen_screenshot_path': _('Upload a screenshot of the second screen.'),
            'video_recording_path': _('Upload a video recording.'),
            'ui_hierarchy': _('Upload the UI hierarchy file.'),
            'screen_changed': _('Indicate if the screen has changed.'),
        }