# Generated by Django 5.0.1 on 2024-02-28 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messi', '0005_mainpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
