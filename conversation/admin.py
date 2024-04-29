from django.contrib import admin

from .models import Conversation, ConversationMessage


#class ConversationAdmin(admin.ModelAdmin):
    #list_display = ('item', 'members', 'created_at', 'modified_at')


class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'content', 'created_at')





admin.site.register(Conversation)

admin.site.register(ConversationMessage, ConversationMessageAdmin)

