from django.db import models
from blogs.models import BlogPost
from profiles.models import UserProfile


class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='comments')
    blog = models.ForeignKey(BlogPost, null=False, blank=False,
                             on_delete=models.CASCADE, default='')
    writer = models.CharField(max_length=50, null=False, blank=False,
                              default='')
    comment = models.TextField()
    writtenon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['writtenon']

    def __str__(self):
        return self.comment
