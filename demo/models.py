from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
