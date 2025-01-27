from django.http import JsonResponse

def user_profile(request):
    if request.user.is_authenticated:
        salary = request.user.profile.salary
        return JsonResponse({"username": request.user.username, "salary": salary})
    return JsonResponse({"error": "User not logged in"}, status=400)