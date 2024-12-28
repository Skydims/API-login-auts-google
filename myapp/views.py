from django.http import JsonResponse
from myapp.utils.firebase_utils import verify_firebase_token

def example_view(request):
    id_token = request.headers.get("Authorization")  # Ambil token dari header
    if id_token:
        user_data = verify_firebase_token(id_token)
        if user_data:
            return JsonResponse({"status": "success", "user": user_data})
        else:
            return JsonResponse({"status": "error", "message": "Invalid token"}, status=401)
    else:
        return JsonResponse({"status": "error", "message": "No token provided"}, status=400)
