from django.http import JsonResponse

class SalaryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            experience = getattr(request.user.profile, 'experience', 0)
            salary = self.calculate_salary(experience)
            request.user.profile.salary = salary
        response = self.get_response(request)
        return response

    def calculate_salary(self, experience):
        if 1 <= experience <= 3:
            return 1000
        elif 3 < experience <= 7:
            return 2000
        elif 5 <= experience <= 10:
            return 5000
        else:
            return 0