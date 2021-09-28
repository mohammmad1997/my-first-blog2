from django import forms
from .models import Post

class PostForm(forms.modelForm):
    class meta:
        model=Post
        fields=('title','text')