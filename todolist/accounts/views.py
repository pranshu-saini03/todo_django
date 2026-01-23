from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from .jwt_utils import generate_jwt
@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "username and password required"}, status=400)

    user = User.objects.filter(username=username, password=password).first()

    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    token = generate_jwt(user.id)

    request.session["last_login"] = user.username

    return JsonResponse({
        "token": token,
        "role": user.role.name
    })
@csrf_exempt
def logout(request):
    request.session.flush()
    return JsonResponse({"message": "Logged out successfully"})