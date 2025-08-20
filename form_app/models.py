from django.db import models


class FormSubmission(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Submission {self.id} - {self.created_at}"