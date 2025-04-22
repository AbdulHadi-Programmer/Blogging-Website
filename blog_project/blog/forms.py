from .models import *
from django import forms

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost 
        fields = ['title', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}), 
            'slug': forms.TextInput(attrs={'class': 'slug'}), 
            'content': forms.Textarea(attrs={'class': 'content'}), 
        }




