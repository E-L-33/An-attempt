from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.db import models
from django.utils import timezone    # from datetime import datetime

class Read_Num(models.Model):
    read_num = models.IntegerField(default=0)
    #ContentType固定写法   文档见：https://docs.djangoproject.com/zh-hans/2.1/ref/contrib/contenttypes/
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Read_Num_Expand_Method():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)    
            readnum = Read_Num.objects.get(content_type=ct,object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

class Read_Detail(models.Model):
    read_num = models.IntegerField(default=0)
    read_time = models.DateField(default=timezone.now)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
