# Generated by Django 3.0.5 on 2020-04-30 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=10, verbose_name='公司名称')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=10, verbose_name='员工姓名')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Company', verbose_name='公司')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
