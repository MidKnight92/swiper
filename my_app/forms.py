from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"id": "user-password"}
        )
    )
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('Invalid')
        return username
    
class SignupForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=17, required=True)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={"id": "user-password"}
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={"id": "user-confirm-password"}
        )
    )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email
        
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError('Invalid Username')
        return username

