from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    list_display = ('comment_user','comment_time','comment_text','object_id','content_object')
    ordering = ('-comment_time',)
        