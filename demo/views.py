import json
import logging

from django.shortcuts import render, redirect
from django.urls import reverse

from demo.forms import BookModelFormSet
from demo.models import Book

logger = logging.getLogger(__name__)


def index(request):
    urls = {
        'book': reverse('demo:book'),
        'book_list': reverse('demo:book_list'),
    }
    return render(request=request, template_name='demo/index.html', context=locals())


def book(request):
    heading_message = 'Formset Demo'
    books = Book.objects.all()
    if request.method == 'GET':
        formset = BookModelFormSet(queryset=books)
    else:
        logger.info(json.dumps(request.POST, indent=4))
        formset = BookModelFormSet(request.POST, queryset=books)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('demo:book_list'))
    return render(
        request=request,
        template_name='demo/book.html',
        context={
            'formset': formset,
            'heading': heading_message,
        }
    )


def book_list(request):
    books = Book.objects.all()
    return render(request=request, template_name='demo/book_list.html', context={'books': books})
