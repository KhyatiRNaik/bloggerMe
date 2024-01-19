from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_bootstrap5.bootstrap5 import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from .models import Profile

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)#,  widget=forms.EmailInput(attrs={'class': 'form-control form-floating'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field("email", css_class="form-floating")
    #         # FloatingField("email"),
    #     )

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']  

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic']
