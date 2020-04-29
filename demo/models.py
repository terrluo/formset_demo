from django.db import models


class Book(models.Model):
    name = models.CharField('书名', max_length=50)
    pub_date = models.DateField('出版日期')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
