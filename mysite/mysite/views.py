from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Blog
from .forms import Login_Form,Register_Form
from data_statistics.utils import data_for_seven_days,today_hot_read_data,week_hot_read_data
from blog.views import get_blog_list_common_method


def home(request):
    # blog = get_object_or_404(Blog, pk=Blog_pk)
    # blog.content = markdown.markdown(blog.content)
    blog_all_list = Blog.objects.all()
    Blogs = ContentType.objects.get_for_model(Blog)
    dates,read_nums = data_for_seven_days(Blogs)

    context = get_blog_list_common_method(request, blog_all_list)
    # context['blog'] = blog
    context['dates'] = dates
    context['read_nums'] = read_nums
    # context['data_for_7_days'] = week_hot_read_data() # 七日热门阅读
    # context['today_read_data'] = today_hot_read_data(Blogs) # 今日热门阅读
    return render(request,'home.html',context)

# 之前的主页调用的方法
def home_bak(request):
    Blogs = ContentType.objects.get_for_model(Blog)
    dates,read_nums = data_for_seven_days(Blogs)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['data_for_7_days'] = week_hot_read_data()
    context['today_read_data'] = today_hot_read_data(Blogs)
    return render(request,'home_bak.html',context)



def login_in(request):
    if request.method == 'POST':
        forms = Login_Form(request.POST)   # 绑定表单数据
        if forms.is_valid():
            user = forms.cleaned_data['user']
            auth.login(request,user)
            return redirect(request.GET.get('from',reverse('home')))
    else:
        forms = Login_Form()

    context = {}
    context['forms'] = forms
    return render(request,'login.html',context)

def register(request):
    if request.method == 'POST':
        register = Register_Form(request.POST)
        if register.is_valid():
            username = register.cleaned_data['username']
            email = register.cleaned_data['email']
            password = register.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        register = Register_Form()

    context = {}
    context['register'] = register
    return render(request,'register.html',context)
