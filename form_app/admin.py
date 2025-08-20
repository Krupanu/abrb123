from django.contrib import admin
from .models import FormSubmission

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'data']
    list_filter = ['created_at']
    readonly_fields = ['created_at']