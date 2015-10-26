# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151022_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.IntegerField(default=0, choices=[(0, b'Mr.'), (1, b'Mrs.'), (2, b'Ms.'), (3, b'Dr.')])),
                ('first_name', models.CharField(default=b'', max_length=300)),
                ('last_name', models.CharField(default=b'', max_length=300)),
                ('email_Address', models.CharField(default=b'', max_length=300)),
                ('message', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
