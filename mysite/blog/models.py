from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from data_statistics.models import Read_Num_Expand_Method
from data_statistics.models import Read_Detail


class Blog_Type(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
        #用来修改在其他类的展示方法？？？

class Blog(models.Model,Read_Num_Expand_Method):
#   一片文章应该有【标题、正文、作者、创建时间、修改时间、类型、浏览量、点赞量】
    title = models.CharField(max_length=30)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    read_num = models.IntegerField(default=0)
    read_detail = GenericRelation(Read_Detail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    blog_type = models.ForeignKey(Blog_Type,on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<Blog: %s>"%self.title

    # 按创建时间倒叙排列  没懂
    class Meta:
        ordering = ['-created_time']
