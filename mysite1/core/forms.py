from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(SignupForm, self).save(commit=False)
            user.email = cleaned_data['email']
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']

            if commit:
                user.save()

            return user
