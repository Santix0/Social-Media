from django import forms

from .models import *


# form for creating the community
class CreateCommunityForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter name',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    bio = forms.CharField(label='Bio', widget=forms.TextInput(attrs={
        'placeholder': 'Enter bio',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(attrs={
        'placeholder': 'Attach avatar',
        'class': 'form-control',
        'style': 'width: 350px'
    }))

    class Meta:
        model = Community
        fields = (
            'name', 'bio', 'avatar',
        )


# form for adding the post to community
class AddPostForm(forms.ModelForm):
    photo = forms.ImageField(label='Photo', widget=forms.FileInput(attrs={
        'placeholder': 'Attach photo',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
        'placeholder': 'Enter description',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = Post
        fields = (
            'photo', 'description',
        )


# from to change community information
class ChangeCommunityInfoForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter name',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    bio = forms.CharField(label='Bio', widget=forms.TextInput(attrs={
        'placeholder': 'Enter bio',
        'class': 'form-control',
        'style': 'width: 350px;',
    }))

    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(attrs={
        'placeholder': 'Attach photo',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = Community
        fields = (
            'name', 'bio', 'avatar',
        )


class EditPostForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = Post
        fields = ('description',)


class AddCommentToPostForm(forms.ModelForm):
    comment = forms.CharField(label='Comment', widget=forms.TextInput(attrs={
        'placeholder': 'Enter comment',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = CommentsToCommunityPosts
        fields = ('comment',)


class EditCommentForm(forms.ModelForm):
    comment = forms.CharField(label='Comment', widget=forms.TextInput(attrs={
        'placeholder': 'Enter comment',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = CommentsToCommunityPosts
        fields = ('comment',)
