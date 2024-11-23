from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Your Username"}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Your Email"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter Your Password"}
        )
    )
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter Your Password again"}
        )
    )

    def clean_email(self):
        """
        check if email is exists
        :return: email
        """
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("Email already registered")
        return email

    def clean_username(self):
        """
        handel username Error
        :return:
        """
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("Username already registered")
        return username

    def clean(self):
        """
            Check password and repeat password are match
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        if password and repeat_password and password != repeat_password:
            raise ValidationError("Passwords do not match")


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Your Password"}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Email"}))

    class Meta:
        model = Profile
        fields = ["age", "bio"]
