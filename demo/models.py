from django.db import models

from core.models import CoreModel


class Company(CoreModel):
    name = models.CharField('公司名称', max_length=10)


class Employee(CoreModel):
    name = models.CharField('员工姓名', max_length=10)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE, verbose_name='公司')
