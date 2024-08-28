from django.contrib import admin

from .models import UploadedApk
# Register your models here.
from django.contrib import admin
from .models import UploadedApk

@admin.register(UploadedApk)
class UploadedApkAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_by', 'created_at', 'updated_at')
    search_fields = ('name', 'uploaded_by__username')
    list_filter = ['created_at']
    readonly_fields = ('created_at', 'updated_at')
    