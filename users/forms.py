from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        # specify model for UserRegisterForm to interact with
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        