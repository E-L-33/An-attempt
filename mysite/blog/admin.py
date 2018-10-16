from django.contrib import admin
from .models import Blog,Blog_Type

# Register your models here.
@admin.register(Blog)
class Blog_Admin(admin.ModelAdmin):
    list_display = ('id','title','author','get_read_num','blog_type','created_time','last_update_time')
    ordering = ('-id',)

    def __str__(self):
        return self.type_name
        #用来修改在其他类的展示方法？？？

@admin.register(Blog_Type)
class Blog_Type_Admin(admin.ModelAdmin):
    list_display = ('id','type_name')
    ordering = ('id',)

    def __str__(self):
        return "<Blog: %s>"%self.title
