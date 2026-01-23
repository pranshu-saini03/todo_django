from .jwt_utils import decode_jwt

class JWTAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.user_id = None

        auth = request.headers.get("Authorization")
        if auth and auth.startswith("Bearer "):
            token = auth.split(" ")[1]
            payload = decode_jwt(token)
            if payload:
                request.user_id = payload.get("user_id")

        return self.get_response(request)
