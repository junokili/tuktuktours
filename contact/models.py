from django.db import models


class Message(models.Model):
    message_email = models.EmailField(max_length=254, null=False, blank=False)
    message_author = models.CharField(max_length=50, null=False, blank=False,
                                      default='')
    order_number = models.CharField(max_length=50, null=True, blank=True)
    message_body = models.TextField()
    writtenon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['writtenon']

    def __str__(self):
        return self.message_author
