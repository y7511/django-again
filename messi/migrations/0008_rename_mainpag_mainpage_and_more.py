# Generated by Django 5.0.1 on 2024-02-29 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messi', '0007_rename_mainpage_mainpag_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mainpag',
            new_name='mainpage',
        ),
        migrations.RenameField(
            model_name='abouttable',
            old_name='lmessi',
            new_name='imessi',
        ),
        migrations.RenameField(
            model_name='mainpage',
            old_name='lmessi',
            new_name='imessi',
        ),
    ]
