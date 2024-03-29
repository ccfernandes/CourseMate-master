# Generated by Django 2.2.3 on 2019-08-26 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20190826_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 26, 14, 57, 55, 153851), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='schoolcourse',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 26, 14, 57, 55, 151963), verbose_name='data published'),
        ),
    ]
