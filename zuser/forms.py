from django import forms
from django.contrib.auth.models import User
from zuser.models import UserProfile

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    conpassword = forms.CharField(label='Confirm', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'conpassword', 'email', )

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('department',)