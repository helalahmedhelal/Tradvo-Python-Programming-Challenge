# from django.test import TestCase
# from django.contrib.auth.models import User
# from interface.models import UploadedApk
# from django.core.files.uploadedfile import SimpleUploadedFile
# import tempfile
# from PIL import Image
# import os

# class UploadedApkModelTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='password')


#     def test_create_uploaded_apk(self):
#         """Test creating a UploadedApk instance."""
#         apk_file = SimpleUploadedFile("test.apk", b"file_content", content_type="application/vnd.android.package-archive")
#         first_screenshot = self.create_image_file('first_screenshot.png')
#         second_screenshot = self.create_image_file('second_screenshot.png')
#         video_file = SimpleUploadedFile("video.mp4", b"video_content", content_type="video/mp4")
#         ui_hierarchy_file = SimpleUploadedFile("hierarchy.xml", b"<xml></xml>", content_type="text/xml")

#         apk = UploadedApk.objects.create(
#             name="Test APK",
#             uploaded_by=self.user,
#             apk_file_path=apk_file,
#             first_screen_screenshot_path=first_screenshot,
#             second_screen_screenshot_path=second_screenshot,
#             video_recording_path=video_file,
#             ui_hierarchy=ui_hierarchy_file,
#             screen_changed=True
#         )

#         self.assertEqual(apk.name, "Test APK")
#         self.assertEqual(apk.uploaded_by, self.user)
#         self.assertTrue(os.path.exists(apk.apk_file_path.path))
#         self.assertTrue(os.path.exists(apk.first_screen_screenshot_path.path))
#         self.assertTrue(os.path.exists(apk.second_screen_screenshot_path.path))
#         self.assertTrue(os.path.exists(apk.video_recording_path.path))
#         self.assertTrue(os.path.exists(apk.ui_hierarchy.path))
#         self.assertTrue(apk.screen_changed)

#     def test_uploaded_apk_str(self):
#         """Test the string representation of the UploadedApk model."""
#         apk = UploadedApk.objects.create(
#             name="Test APK",
#             uploaded_by=self.user,
#         )
#         self.assertEqual(str(apk), "Test APK")

#     def create_image_file(self, filename):
#         """Helper method to create a temporary image file."""
#         image = Image.new('RGB', (100, 100))
#         temp_file = tempfile.NamedTemporaryFile(suffix='.png')
#         image.save(temp_file, format='PNG')
#         temp_file.seek(0)
#         return SimpleUploadedFile(filename, temp_file.read(), content_type='image/png')

#     def tearDown(self):
#         """Cleanup any files created during the tests."""
#         for apk in UploadedApk.objects.all():
#             if apk.apk_file_path:
#                 apk.apk_file_path.delete()
#             if apk.first_screen_screenshot_path:
#                 apk.first_screen_screenshot_path.delete()
#             if apk.second_screen_screenshot_path:
#                 apk.second_screen_screenshot_path.delete()
#             if apk.video_recording_path:
#                 apk.video_recording_path.delete()
#             if apk.ui_hierarchy:
#                 apk.ui_hierarchy.delete()
