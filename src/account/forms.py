from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account

from django.utils.crypto import get_random_string

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')