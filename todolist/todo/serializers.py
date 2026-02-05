from rest_framework import serializers
from .models import Todo

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description']


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at']


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'completed': {'required': False},
        }


class TodoDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
