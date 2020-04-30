from django.db import models


class CoreModel(models.Model):
    created_date = models.DateTimeField('创建时间', auto_now_add=True)
    modified_date = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True
