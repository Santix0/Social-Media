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
        model = CommunityPost
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

    theme = forms.ChoiceField(label='Theme', choices=THEMES, widget=forms.Select(attrs={
        'placeholder': 'Select theme of community',
        'class': 'form-select',
        'style': 'width: 350px',
    }))

    sub_theme = forms.CharField(label='Sub theme', widget=forms.TextInput(attrs={
        'placeholder': 'Enter sub theme of community',
        'class': 'form-control',
        'style': 'width: 350px'
    }))

    class Meta:
        model = Community
        fields = (
            'name', 'bio', 'avatar',
            'theme', 'sub_theme',
        )


class EditPostForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = CommunityPost
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


class CommunityChangeInformationForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Bio',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    avatar = forms.ImageField(label='Photo', widget=forms.FileInput(attrs={
        'placeholder': 'Attach photo',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    theme = forms.ChoiceField(label='Theme', choices=THEMES, widget=forms.Select(attrs={
        'placeholder': 'Select theme',
        'class': 'select-control',
        'style': 'width: 350px',
    }))

    sub_theme = forms.CharField(label='Sub theme', widget=forms.TextInput(attrs={
        'placeholder': 'Enter sub theme',
        'class': 'form-control',
        'style': 'width: 350px',
    }))

    class Meta:
        model = Community
        fields = (
            'bio', 'avatar', 'theme',
            'sub_theme',
        )
