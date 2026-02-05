from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Role
from .jwt_utils import generate_jwt
from .serializers import LoginSerializer, UserSerializer


class registrationview(APIView):
    def post(self, request):
        data = request.data.copy()
        role_name = data.get('role')
        if not role_name:
            return Response(
                {"role": "This field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            default_role = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            return Response(
                {"role": "Invalid role."},
                status=status.HTTP_400_BAD_REQUEST
            )

        data['role'] = default_role.id
        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        return Response({
            "id": user.id,
            "username": user.username,
            "role": user.role.name
        }, status=status.HTTP_201_CREATED)

class loginview(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        username=serializer.validated_data['username']
        password=serializer.validated_data['password']
        user=User.objects.filter(username=username,password=password).first()

        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = generate_jwt(user.id)
        request.session["last_login"] = user.username

        return Response({
            "token": token,
            "role": user.role.name
        }, status=status.HTTP_200_OK
        )
 
class logoutview(APIView):
    def post(self, request):
        request.session.flush()
        return Response({"message": "Logged out successfully"},
                        status=status.HTTP_200_OK)