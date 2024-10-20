from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройки админки для отображения задач."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
