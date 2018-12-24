from django import forms
from mdeditor.fields import MDTextFormField
from blog.models import Blog


class MDEditorForm (forms.Form):
    content = MDTextFormField()

# class MDEditorModleForm(forms.ModelForm):
    # class Meta:
    #     model = Blog
    #     fields = 'content'
