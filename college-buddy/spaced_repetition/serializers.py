from rest_framework import serializers
from .models import TodoItem, Reminders


# Models serializers
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'user', 'reminders', 'title', 'completed')

class RemindersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminders
        fields = ('id', 'user', 'created_date', 'items')

# Create Model Serializers
class CreateToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('reminders', 'title')

class CreateRemindersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('items')