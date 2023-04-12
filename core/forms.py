from django import forms
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='NG')
    )
    class Meta:
        model = Profile
        exclude = ('user','email')


