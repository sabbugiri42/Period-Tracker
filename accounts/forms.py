from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, required = True, label="username")
    email = forms.EmailField(required = True, label="email")
    password = forms.CharField(max_length=150, required=True, label="password")
    age = forms.IntegerField(required = True, label="age")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required = True, label= "username")
    password = forms.CharField(max_length=150, required=True, label="password")