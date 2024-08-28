from typing import Any
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.forms.widgets import TextInput,PasswordInput
from django.utils.translation import gettext_lazy as _

class CreateUserForm(UserCreationForm):
    class Meta:
        
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']
        
        labels = {
            'username': _('Username'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
        }
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)  
        
        self.fields['email'].required=True  
        
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():

            raise forms.ValidationError(_('This email is invalid'))

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError(_("Your email is too long"))


        return email
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label=_('Password'),
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    

class UpdatedUserForm(forms.ModelForm):
    
    password= None
    
    def __init__(self, *args, **kwargs):
        
        super(UpdatedUserForm,self).__init__(*args, **kwargs)  
        
        self.fields['email'].required=True 
        
        
    class Meta:
        
        model=User
        
        fields=['username','email']
        
        labels = {
            'username': _('Username'),  # Translatable label
            'email': _('Email'),  # Translatable label
        }
        
        exclude=['password1', 'password2']    