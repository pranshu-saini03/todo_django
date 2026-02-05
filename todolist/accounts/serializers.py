from rest_framework import serializers

from .models import Role, Permission, User


class RoleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            'id',
            'role',
            'can_create',
            'can_read',
            'can_update',
            'can_delete'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()