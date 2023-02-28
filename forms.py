from dataclasses import fields
from django import forms
from .models import Post, Category, Comment

# choice = [('coding','coding'),('gaming','gaming'),('workout','workout'),]
choice = Category.objects.all().values_list('name','name')
choice_list = []

for i in choice:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','header_image', 'author', 'category', 'body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blog Titile Here....'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'authorName', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blog Titile Here....'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
