#!/usr/bin/python
from django import forms
from django.forms import modelformset_factory, formset_factory, BaseFormSet

from demo.models import Book


class BookForm(forms.Form):
    name = forms.CharField(label='书名')


class BaseBookFormset(BaseFormSet):
    def clean(self):
        """Checks that no two articles have the same name."""

        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        names = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            name = form.cleaned_data.get('name')
            if name in names:
                raise forms.ValidationError("Book in a set must have distinct names.")
            names.append(name)


BookFormSet = formset_factory(BookForm, formset=BaseBookFormset, extra=1, can_delete=True)


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_date', 'modified_date']

    def __init__(self, *args, **kwargs):
        super(BookModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '书名'


BookModelFormSet = modelformset_factory(model=Book, form=BookModelForm, extra=1, min_num=1, can_delete=True)
