import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import Read_Num,Read_Detail
from blog.models import Blog

def data_statistics_once_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" %(ct.model,obj.pk)

    #当cookies里面没有我们的阅读记录时，我们认为算一次阅读，找该文章的阅读记录，有就加一，没有就创建了再加一
    if not request.COOKIES.get(key):
        read_num,created = Read_Num.objects.get_or_create(content_type=ct,object_id=obj.pk)
        read_num.read_num += 1
        read_num.save()

        date = timezone.now().date()
        read_detail,created = Read_Detail.objects.get_or_create(content_type=ct,object_id=obj.pk)
        read_detail.read_num += 1
        read_detail.save()
    return key

def data_for_seven_days(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(6,-1,-1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))    #strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
        read_details = Read_Detail.objects.filter(content_type=content_type,read_time=date)
        # 聚合计算
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates,read_nums

def today_hot_read_data(content_type):
    today = timezone.now().date()
    today_data = Read_Detail.objects.filter(content_type=content_type,read_time=today).order_by('-read_num')
    return today_data[:7]

def week_hot_read_data():
    today = timezone.now().date()
    last_7_day = today - datetime.timedelta(days=7)
    data_for_7_days = Blog.objects \
                          .filter(read_detail__read_time__lt=today, read_detail__read_time__gte=last_7_day) \
                          .values('id','title') \
                          .annotate(read_num_sum=Sum('read_detail__read_num')) \
                          .order_by('-read_num_sum')
    return data_for_7_days[:7]