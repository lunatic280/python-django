from django import forms
from django.core.exceptions import ValidationError

from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4)

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용중입니다")
        return username

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        return user


