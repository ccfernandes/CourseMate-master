# Generated by Django 2.2.3 on 2019-08-08 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190808_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 19, 27, 14, 362132), verbose_name='data published'),
        ),
    ]