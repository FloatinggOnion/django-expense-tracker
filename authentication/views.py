from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import validate_email
from django.contrib import messages
from django.core.mail import send_mail

# This view renders the registration form
class RegistrationView(View):
    
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        
        # Get user datd
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        # Validate data

        if not User.objects.filter(username = username).exists():
            if not User.objects.filter(email = email).exists():

                if len(password) < 8:
                    messages.error(request, 'Password too short')
                    return render(request, 'auth/register.html')

        
        # Create account and display alert
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # You can use the above method to add the password, or you can use...
                # user.set_password(password)

                email_subject = 'Activate your account'
                email_body = ''
                send_mail(
                    email_subject,
                    email_body,
                    'noreply@atwotcost.com',
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'Account created successfully')
                return render(request, 'auth/register.html')

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

