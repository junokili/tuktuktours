from django import forms
from .models import BlogPost, Comment
from tours.widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'author',
                  'image',)

        image = forms.ImageField(label='Select Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('writer', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
