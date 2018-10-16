from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist

class Comment_Form(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content_type = forms.CharField(widget=forms.HiddenInput)
    comment_text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'),
                                    error_messages={'required':'评论内容不能为空'})

    def __init__(self,*args,**kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(Comment_Form,self).__init__(*args,**kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')

        # 判断评论对象是否存在  ObjectDoesNotExist对象不存在的错误类型
        content_type = self.cleaned_data['content_type']
        object_id  =  self.cleaned_data['object_id']
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')

        return self.cleaned_data