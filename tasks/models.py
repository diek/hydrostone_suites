from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Task(models.Model):
    task = models.CharField(max_length=260)
    annual_task = models.BooleanField(default=False)
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_tasks'
    )
    task_details = models.TextField()
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_started = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Task assigned by {self.assigned_by} on {self.date_assigned.strftime('%Y-%m-%d')}"


class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    specialty = models.TextField()
    primary_phone = PhoneNumberField(blank=True, null=True)
    secondary_phone = PhoneNumberField(blank=True, null=True)
    contact_email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.contact_name} {self.primary_phone}"
