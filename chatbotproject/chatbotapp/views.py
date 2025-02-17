from django.http import JsonResponse
from ...chatbot import generate_text

def execute_model(request):
    if request.method == "GET":
        text = generate_text()
        return JsonResponse({"text": text})
    return JsonResponse({"error": "Invalid request method"}, status=400)