import json
import logging

from django.shortcuts import render

from demo.forms import BookModelFormSet
from demo.models import Book

logger = logging.getLogger(__name__)


def index(request):
    books = Book.objects.all()
    if request.method == 'POST':
        book_formset = BookModelFormSet(data=request.POST, queryset=books)
        logger.info(json.dumps(request.POST, indent=4))
        if book_formset.is_valid():
            logger.info('book_formset valid')
            for book_form in book_formset:
                logger.info('book save')
                # 没有被初始化并且没有填写数据的表单将不会调用 save 方法进行保存
                if book_form.cleaned_data:
                    book_form.save()
        else:
            logger.info('book_formset invalid')
    else:
        book_formset = BookModelFormSet(queryset=books)
    return render(request=request, template_name='demo/index.html', context=locals())
