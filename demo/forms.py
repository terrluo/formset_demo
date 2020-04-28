#!/usr/bin/python
from django import forms
from django.forms import modelformset_factory

from demo.models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_date', 'modified_date']


# 1、如果不想但 post 请求没有数据时，FormSet 但 is_valid() 还是 True 的话，就要设置 min_num
# 2、在 views 里创建 BookModelFormSet 的话，在验证通过调用 save 方法时，save 会警告 Parameter 'self' unfilled，我现在还不知道是为什么
BookModelFormSet = modelformset_factory(model=Book, form=BookModelForm, min_num=1)
