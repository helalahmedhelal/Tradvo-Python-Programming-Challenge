from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from interface.models import UploadedApk
from django.core.files.uploadedfile import SimpleUploadedFile

class ApkViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Sample file to use for uploads
        self.sample_apk = SimpleUploadedFile("test.apk", b"file_content", content_type="application/vnd.android.package-archive")
        self.apk = UploadedApk.objects.create(
            name="Test APK",
            uploaded_by=self.user,
            apk_file_path=self.sample_apk,
        )

    def test_apk_list_view(self):
        """Test the APK list view."""
        response = self.client.get(reverse('apk_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interface/uploadedapks/apk_list.html')
        self.assertContains(response, self.apk.name)

    def test_apk_add_view_get(self):
        """Test the APK add view (GET request)."""
        response = self.client.get(reverse('apk_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interface/uploadedapks/apk_add.html')

    # def test_apk_add_view_post(self):
    #     """Test the APK add view (POST request)."""
    #     data = {
    #         'name': 'New APK',
    #         'apk_file_path': self.sample_apk,
    #     }
    #     response = self.client.post(reverse('apk_add'), data)
    #     self.assertEqual(response.status_code, 200)  # Expecting a redirect
    #     self.assertTrue(UploadedApk.objects.filter(name='New APK').exists())

    def test_apk_details_view(self):
        """Test the APK details view."""
        response = self.client.get(reverse('apk_details', args=[self.apk.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interface/uploadedapks/apk_details.html')
        self.assertContains(response, self.apk.name)

    def test_apk_update_view_get(self):
        """Test the APK update view (GET request)."""
        response = self.client.get(reverse('apk_update', args=[self.apk.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interface/uploadedapks/apk_update.html')
        self.assertContains(response, self.apk.name)

    def test_apk_update_view_post(self):
        """Test the APK update view (POST request)."""
        updated_data = {
            'name': 'Updated APK',
            'apk_file_path': self.sample_apk,
        }
        response = self.client.post(reverse('apk_update', args=[self.apk.pk]), updated_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.apk.refresh_from_db()
        self.assertEqual(self.apk.name, 'Updated APK')

    def test_apk_delete_view_get(self):
        """Test the APK delete view (GET request)."""
        response = self.client.get(reverse('apk_delete', args=[self.apk.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interface/uploadedapks/apk_delete.html')

    def test_apk_delete_view_post(self):
        """Test the APK delete view (POST request)."""
        response = self.client.post(reverse('apk_delete', args=[self.apk.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertFalse(UploadedApk.objects.filter(pk=self.apk.pk).exists())

    def tearDown(self):
        """Cleanup any files created during the tests."""
        self.apk.apk_file_path.delete()
