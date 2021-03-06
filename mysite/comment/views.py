from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import Comment
from .forms import Comment_Form

# Create your views here.
def submit_comment(request):
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    data = {}

    #向forms里面传递user参数    
    comment_form = Comment_Form(request.POST,user=request.user)


    if comment_form.is_valid():
        comment = Comment()
        comment.comment_user = comment_form.cleaned_data['user']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.comment_text = comment_form.cleaned_data['comment_text']
        comment.save()

        return redirect(referer)

        # # 返回数据
        # data['status'] = 'SUCCESS'
        # data['username'] = comment.user.username
        # data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        # data['comment_text'] = comment.comment_text
    else:
        return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
    #     data['status'] = 'ERROR'
    #     data['message'] = list(comment_form.errors.values())[0][0]
    # return JsonResponse(data)

