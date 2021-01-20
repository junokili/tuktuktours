from django.db import models
from profiles.models import UserProfile

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogPost(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='posts')
    title = models.CharField(max_length=254, null=False, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=50, null=False, blank=False, default='')
    content = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['createdon']

    def __str__(self):
        return self.title


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='comments', default='')
    writer = models.CharField(max_length=50, null=False, blank=False,
                              default='')
    comment = models.TextField()
    writtenon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['writtenon']

    def __str__(self):
        return self.comment
