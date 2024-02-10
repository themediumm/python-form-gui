# myapp/forms.py
from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'place_of_origin', 'gender']
