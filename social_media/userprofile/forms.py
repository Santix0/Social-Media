from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *
from .utils import *

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import *


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

    avatar = forms.ImageField(label='Photo', widget=forms.FileInput(attrs={
        'placeholder': 'Attach photo',
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

    birthday_of_user = forms.DateTimeField(label='Birthday', required=False, widget=forms.DateTimeInput(attrs={
        'placeholder': 'Enter birthday',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    phone_number = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget(
        initial='RO',
        attrs={
            'class': 'form-control',
            'style': 'width: 350px;',
        },
    ))

    bio = forms.CharField(label='Bio', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Add bio',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    gender = forms.ChoiceField(label='Gender', choices=Gender, required=False, widget=forms.Select(attrs={
        'placeholder': 'Choose gender',
        'class': 'form-select',
        'style': 'width: 350px',
    }))

    place_of_work = forms.CharField(label='Place of work', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your place of work',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    place_of_study = forms.CharField(label='Place of study', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your place of study',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    hobbies = forms.CharField(label='Hobbies', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your hobbies',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    relationship = forms.ChoiceField(label='Relationship', choices=RELATIONSHIP_STATUS, required=False,
                                     widget=forms.Select(attrs={
                                         'placeholder': 'Choose your status',
                                         'class': 'form-select',
                                         'style': 'width: 350px',
                                     }))

    political_views = forms.CharField(label='Political_views', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your political_views',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    religion = forms.CharField(label='Religion', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter you religion',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    favorite_music = forms.CharField(label='Favorite music', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your favorite music',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    favorite_movies = forms.CharField(label='Favorite movies', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your favorite movies',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    favorite_books = forms.CharField(label='Favorite books', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your favorite books',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    town_of_living = forms.CharField(label='Hometown', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your hometown',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'avatar', 'phone_number', 'bio',
                  'birthday_of_user', 'gender', 'place_of_work',
                  'place_of_study', 'hobbies', 'relationship',
                  'political_views', 'religion', 'favorite_music',
                  'favorite_movies', 'favorite_books', 'town_of_living',
                  )


# Form for adding post
class AddPostForm(forms.ModelForm):
    photo = forms.ImageField(label='Post', widget=forms.FileInput(attrs={
        'placeholder': 'Attach photo',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = UserPost
        fields = ('photo', 'description',)


class ChangePostForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = UserPost
        fields = ('description',)


# form for adding comment to user's post
class CommentToUserPostForm(forms.ModelForm):
    comment = forms.CharField(label='Comment', widget=forms.TextInput(attrs={
        'placeholder': 'Enter comment',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = CommentToUserPost
        fields = ('comment',)


class EditCommentForm(forms.ModelForm):
    comment = forms.CharField(label='Comment', widget=forms.TextInput(attrs={
        'placeholder': 'Edit comment',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = CommentToUserPost
        fields = ('comment',)
