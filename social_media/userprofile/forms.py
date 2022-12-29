from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *
from .utils import *


# form for sing up
class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter first name',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter last name',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password again',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'first_name', 'last_name',
                  )


# form for sing in
class SignInForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = User
        fields = ('username', 'password1',)


# form for changing user profile info
class ChangeUserProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter first name',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter last name',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    birthday = forms.IntegerField(label='Birthday', widget=forms.TextInput(attrs={
        'placeholder': 'Enter birthday',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    phone_number = forms.IntegerField(label='Phone number', validators=[validation_of_number], widget=forms.NumberInput(attrs={
        'placeholder': 'Enter phone number',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    bio = forms.CharField(label='Bio', widget=forms.TextInput(attrs={
        'placeholder': 'Add bio',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    gender = forms.ChoiceField(label='Gender', choices=Gender, widget=forms.Select(attrs={
        'placeholder': 'Choose gender',
        'class': 'form-select',
        'style': 'width: 350px',
    }))

    place_of_work = forms.CharField(label='Place of work', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your place of work',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    place_of_study = forms.CharField(label='Place of study', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your place of study',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'birthday', 'phone_number', 'bio',
                  'gender', 'place_of_work', 'place_of_study'
                  )


# Form for adding post
class AddPostForm(forms.ModelForm):
    Photo = forms.ImageField(label='Photo')
