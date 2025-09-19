from .models import User, Todo
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo

        fields = ['id', 'title', 'completed', 'created_at', 'due_date', 'author']
        #set author to read only
        extra_kwargs = {'author' : {'read_only' : True}}