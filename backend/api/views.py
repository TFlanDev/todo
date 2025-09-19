from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import userSerializer, TodoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Todo

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    #so todo list is attributed to author
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)    

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = TodoSerializer
        permission_classes = [IsAuthenticated]
        
        #so only author can delete their own todo item
        def get_queryset(self):
                user = self.request.user
                return Todo.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [AllowAny]
