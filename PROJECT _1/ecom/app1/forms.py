from django import forms
from.models import *


class AddForm(forms.Form):
    number1=forms.IntegerField(label="Enter First Number")
    number2=forms.IntegerField(label="Enter Second Number")


#Model Form

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput()) #TO HIDE PASSWORD INPUT

    class Meta:
        model=User
        fields='__all__'
        fields=['username','email','password']

#PASSWORD VALIDATION

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # 1. Check length
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        # 2. Check if first character is uppercase
        if not password[0].isupper():
            raise forms.ValidationError("Password must start with an uppercase letter.")

        # 3. Check for at least one digit
        if not re.search(r"\d", password):
            raise forms.ValidationError("Password must contain at least one digit.")

        # 4. Check for at least one special character
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise forms.ValidationError("Password must contain at least one special character.")

        return password


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must end with '@gmail.com'")

        return email
