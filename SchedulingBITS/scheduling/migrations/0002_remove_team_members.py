# Generated by Django 4.1.3 on 2022-12-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
    ]
