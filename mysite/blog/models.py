from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from mdeditor.fields import MDTextField
from data_statistics.models import Read_Num_Expand_Method
from data_statistics.models import Read_Detail

class Source_Type(models.Model):
    """源类型,就是最基础本的类型"""
    source_name = models.CharField(max_length=15)

    def __str__(self):
        return self.source_name

class Blog_Type(models.Model):
    """文章的类型,归于特定的源类型"""
    type_name = models.CharField(max_length=15)
    source_to = models.ForeignKey(Source_Type,on_delete=models.DO_NOTHING,default=None)

    def __str__(self):
        return self.type_name
        #用来修改在其他类的展示方法

class Blog(models.Model,Read_Num_Expand_Method):
    """文章类,包含  标题,正文,作者,阅读数量,阅读详情,创建时间,最终修改时间博类型"""
    title = models.CharField(max_length=120)    # 标题
    # content = RichTextUploadingField()    # 正文,ckeditor字段
    content = MDTextField()    # 正文,django-mdeditor字段
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)    # 作者,关联到Django的User模型
    read_num = models.IntegerField(default=0)    # 阅读数量
    read_detail = GenericRelation(Read_Detail)    # GenericRelation一特殊键,可以指向任何Model对象
    created_time = models.DateTimeField(auto_now_add=True)    # 创建时间
    last_update_time = models.DateTimeField(auto_now=True)    # 最后一次更新时间
    blog_type = models.ForeignKey(Blog_Type,on_delete=models.DO_NOTHING)    # 博客类型

    def __str__(self):
        return "<Blog: %s>"%self.title

    class Meta:
        ordering = ['-created_time']    # 按创建时间倒叙排列
