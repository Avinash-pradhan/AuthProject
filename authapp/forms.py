from django.contrib.auth.models import User
from django import forms
import re

class SignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':None}
    def clean_email(self):
        email=self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        elif not email.lower().endswith('@gmail.com'):
            raise forms.ValidationError("only gmail is allowed")
            
        return email
    

# username contains atleast 5 characters
    def clean_username(self):
        username=self.cleaned_data['username']
        if len(username)<5:
            raise forms.ValidationError("Username must be at least 5 characters long")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"\d", password):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not re.search(r"[A-Za-z]", password):
            raise forms.ValidationError("Password must contain at least one letter.")
        if not re.search(r"\W", password):
            raise forms.ValidationError("Password must contain at least one special character.")
        return password
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
