from django.contrib import admin
from .models import Read_Num,Read_Detail

# Register your models here.
@admin.register(Read_Num)
class Read_Num_Admin(admin.ModelAdmin):
    list_display = ('read_num','content_type','object_id','content_object')
    ordering = ('object_id',)

@admin.register(Read_Detail)
class Read_Detail(admin.ModelAdmin):
    list_display = ('read_time','content_object','read_num','content_type','object_id')
    ordering = ('read_time',)
