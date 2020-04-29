#!/usr/bin/python
from django import forms
from django.forms import modelformset_factory, formset_factory, BaseFormSet

from demo.models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_date', 'modified_date']

    def __init__(self, *args, **kwargs):
        super(BookModelForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].widget = forms.DateInput(format='%Y-%m-%d')


BookModelFormSet = modelformset_factory(model=Book, form=BookModelForm, extra=1, min_num=1, can_delete=True)
