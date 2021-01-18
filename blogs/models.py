from django.db import models
from profiles.models import UserProfile

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogPost(models.Model):
    title = models.CharField(max_length=254, null=False, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                               null=True, blank=True, related_name='posts')
    content = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
