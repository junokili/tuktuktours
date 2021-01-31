from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_email', 'message_author', 'message_body',
                    'writtenon',)

    ordering = ('writtenon',)


admin.site.register(Message, MessageAdmin)
