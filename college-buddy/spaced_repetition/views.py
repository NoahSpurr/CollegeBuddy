import logging

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import TodoItem, Reminders
from .forms import Todo_completed_form
from .serializers import ToDoSerializer, CreateToDoSerializer, RemindersSerializer, CreateRemindersSerializer


class ToDoView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)
    

class CreateToDoView(APIView):
    serializer_class = CreateToDoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            reminders = serializer.data.get('reminders')
            title = serializer.data.get('title')
            
            todo = TodoItem.objects.create(
                user = request.user,
                reminders=reminders,
                title=title
            )
            return Response(ToDoSerializer(todo).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
class RemindersView(generics.ListAPIView):
    serializer_class = RemindersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminders.objects.filter(user=self.request.user)
    
class CreateRemindersView(APIView):
    serializer_class = RemindersSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            items = serializer.data.get('items')
            
            reminder = Reminders.objects.create(
                user = request.user,
                items=items
            )
            return Response(RemindersSerializer(reminder).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)