# settings.py
import os

# Security Issue: Hardcoded secret key
SECRET_KEY = 'mysecretkey'  # This should be an environment variable

# Allowed hosts should not be set to '*'
ALLOWED_HOSTS = ['*']

# views.py
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Security Issue: CSRF protection is disabled
@method_decorator(csrf_exempt, name='dispatch')
class UserProfileView(View):
    def post(self, request):
        # Security Issue: No input validation
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Security Issue: Hardcoded credentials
        if username == 'admin' and password == 'password':
            return JsonResponse({"message": "Login successful!"})
        return JsonResponse({"message": "Invalid credentials!"}, status=401)

# Security Issue: Exposing sensitive information
class SensitiveDataView(View):
    def get(self, request):
        # Vulnerability: Exposing sensitive data
        return JsonResponse({"secret": "This is a secret!"})

# urls.py
from django.urls import path
from .views import UserProfileView, SensitiveDataView

urlpatterns = [
    path('login/', UserProfileView.as_view(), name='login'),
    path('sensitive-data/', SensitiveDataView.as_view(), name='sensitive-data'),
]

# models.py
from django.db import models

# Maintainability Issue: Poorly structured model
class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    # Security Issue: Storing passwords in plain text
    # This should be hashed
    def __str__(self):
        return self.username
    
print("Another app print line added")