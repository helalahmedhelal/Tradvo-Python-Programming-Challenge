from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _, gettext

class UploadedApk(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Uploaded by"))
    apk_file_path = models.FileField(_("APK File Path"), upload_to='apk_files/')
    first_screen_screenshot_path = models.ImageField(_("First Screen Screenshot"), upload_to='screenshots/', null=True, blank=True)
    second_screen_screenshot_path = models.ImageField(_("Second Screen Screenshot"), upload_to='screenshots/', null=True, blank=True)
    video_recording_path = models.FileField(_("Video Recording Path"), upload_to='videos/', null=True, blank=True)
    ui_hierarchy = models.FileField(_("UI Hierarchy"), upload_to='ui_hierarchy/', null=True, blank=True)
    screen_changed = models.BooleanField(_("Screen Changed"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return gettext(self.name)
