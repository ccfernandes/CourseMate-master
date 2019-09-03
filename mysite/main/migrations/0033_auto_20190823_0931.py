# Generated by Django 2.2.3 on 2019-08-23 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20190823_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseNum',
        ),
        migrations.AlterField(
            model_name='course',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 23, 9, 31, 48, 51995), verbose_name='data published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 23, 9, 31, 48, 48717), verbose_name='data published'),
        ),
    ]
