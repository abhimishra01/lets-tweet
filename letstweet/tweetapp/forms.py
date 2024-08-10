from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo'] # array when using custom model form
        
        
class UserRegistrationForm(UserCreationForm):
    emailail = forms.EmailField(max_length=254, help_text='Required. Avalid email address.')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2') # tuple when using built in model form
        
        