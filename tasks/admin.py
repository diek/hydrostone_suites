from django.contrib import admin

from .models import Task, Contacts


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'task',
        'annual_task',
        'assigned_by',
        'task_details',
        'date_assigned',
        'date_started',
        'date_completed',
    )
    list_filter = (
        'annual_task',
        'assigned_by',
        'date_assigned',
        'date_started',
        'date_completed',
    )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'contact_name',
        'specialty',
        'primary_phone',
        'secondary_phone',
        'contact_email',
        'notes',
    )
