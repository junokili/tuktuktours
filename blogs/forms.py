from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'author',
                  'image_url', 'image',)

    content = forms.CharField(label='Add your post content here')
    image_url = forms.URLField(label='Add the image URL here or upload the '
                               'image below',
                               required=False)
    image = forms.ImageField(label='Select Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('writer', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
