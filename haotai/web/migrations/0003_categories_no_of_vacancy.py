# Generated by Django 4.1.2 on 2022-10-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_categories_no_of_vacancy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='no_of_vacancy',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
