from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title", "image", "category",
            "summary", "content", "is_draft"
        ]

