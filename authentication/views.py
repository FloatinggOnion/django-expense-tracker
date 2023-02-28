from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User

# This view renders the registration form
class RegistrationView(View):
    
    def get(self, request):
        return render(request, 'auth/register.html')
    

# This view handles the username validation (Checking whether it is already in the database)
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should only contain alphanumeric characters'}, status=400)

        if User.objects.filter(username = username).exists():
            return JsonResponse({'username_error':'username is already taken'}, status=400)
        
        return JsonResponse({'username_valid': True})