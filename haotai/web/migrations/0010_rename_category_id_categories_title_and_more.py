# Generated by Django 4.1.2 on 2022-10-11 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_rename_title_categories_category_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='Category_id',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='jobdescrip',
            name='Category',
        ),
    ]
