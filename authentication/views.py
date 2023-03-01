from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import validate_email
from django.contrib import messages

# This view renders the registration form
class RegistrationView(View):
    
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        messages.success(request, 'Account created successfully')
        return render(request, 'auth/register.html')
    

# This view handles the username validation (Checking whether it is already in the database)
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should only contain alphanumeric characters'}, status=400)

        if User.objects.filter(username = username).exists():
            return JsonResponse({'username_error':'Username is already taken'}, status=400)
        
        return JsonResponse({'username_valid': True})

    

# This view handles the email validation
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email.validate_email(email):
            return JsonResponse({'email_error':'Please use a valid email'}, status=400)

        if User.objects.filter(email = email).exists():
            return JsonResponse({'email_error':'An account with this email already exists'}, status=400)
        
        return JsonResponse({'email_valid': True})

