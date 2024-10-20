from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач."""

    class Meta:
        """Настройки сериализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
