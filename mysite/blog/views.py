from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator #引入分页器
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from .models import Blog,Blog_Type
from data_statistics.utils import data_statistics_once_read 
from comment.models import Comment
from comment.forms import Comment_Form

# Create your views here.
# 分页共用方法
def get_blog_list_common_method(request,blog_all_list):
    paginator = Paginator(blog_all_list,6)    #每6条分一页
    page_num = request.GET.get('page',1)    #获取url的页码参数（GET请求），默认为1
    page_of_blogs = paginator.get_page(page_num)    #得到每一页的具体内容
    # 显示临近的5页和首尾页   最终优化为只显示五格  
    is_num = page_of_blogs.number    #获取当前页码
    num_count = page_of_blogs.paginator.page_range[-1]    #获取最大页码数
    better_paginator = list(range(max(is_num-2,1),min(num_count,is_num+2)+1))
    if is_num-1 > 2:
        better_paginator.insert(0,1)
        if is_num-2-2 >= 1:
            better_paginator.insert(1,"...")
    if num_count - is_num > 2:
        better_paginator.append(num_count)
        if num_count-is_num >= 4:
            better_paginator.insert(-1,"...")

    '''
    # 获取博客分类的博客数量
    Blog_Type.objects.annotate(blog_count = Count('blog'))
    #blog为Blog_Type关联的Blog的小写,blog_count为自定义的变量名   代码最终执行为SQL语句

    #效果等于以下代码
    blog_types = Blog_Type.objects.all()
    blog_type_list = []
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()    #给每一个blog_type类添加属性
        blog_type_list.append(blog_type)
    context['blog_types'] = blog_type_list
    '''
    # 获取时间归档的博客数量
    blog_dates = Blog.objects.dates('created_time','month',order="DESC") #得到的是一个可迭代对象
    blog_date_list = {}
    for  blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blog_date_list[blog_date]= blog_count

    context = {}
    context['better_paginator'] = better_paginator
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = Blog_Type.objects.annotate(blog_count = Count('blog'))
    context['blog_date'] = blog_date_list
    return context

#文章列表页面
def blog_list(request):
    blog_all_list = Blog.objects.all()
    context = get_blog_list_common_method(request, blog_all_list)
    return render(request,'blog/blog_list.html',context)

#按文章类型分类
def blog_with_type(request,blog_with_type):
    context_type = get_object_or_404(Blog_Type,type_name=blog_with_type)
    blog_all_list = Blog.objects.filter(blog_type=context_type)    #筛选????????
    context = get_blog_list_common_method(request, blog_all_list)
    context['type'] = context_type
    return render(request,'blog/blog_with_type.html',context)

# 日期归档
def blog_with_date(request,year,month):
    blog_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)    
    context = get_blog_list_common_method(request, blog_all_list)
    context['blog_date_title'] = "%d年%d月" %(year,month)
    return render(request,'blog/blog_with_date.html',context)

#文章的具体内容页
def blog_detail(request, Blog_pk):
    blog = get_object_or_404(Blog, pk=Blog_pk)
    read_cookies_key = data_statistics_once_read(request, blog)

    blog_ct = ContentType.objects.get_for_model(Blog)
    # blog_ct是<class 'django.contrib.contenttypes.models.ContentType'>类型  blog_ct.model是<class 'str'>
    comments = Comment.objects.filter(content_type=blog_ct,object_id=Blog_pk)


    context = {}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['blog'] = blog
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()

    context['comments'] = comments
    # 初始化时设置Comment_Form的值    initial接受的是一个字典
    context['comment_forms'] = Comment_Form(initial={'content_type':blog_ct,'object_id':Blog_pk})
    response = render(request,'blog/blog_detail.html',context)
    response.set_cookie('blog_%s_read' %Blog_pk,'true')    #设置时间max_age = 60,expires = datetime
    return response
