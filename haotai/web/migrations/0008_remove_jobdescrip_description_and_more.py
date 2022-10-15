# Generated by Django 4.1.2 on 2022-10-11 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_jobdescrip_delete_jobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdescrip',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jobdescrip',
            name='image',
        ),
        migrations.RemoveField(
            model_name='jobdescrip',
            name='no_of_vacancy',
        ),
        migrations.RemoveField(
            model_name='jobdescrip',
            name='title',
        ),
        migrations.AddField(
            model_name='jobdescrip',
            name='Category',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='web.categories'),
            preserve_default=False,
        ),
    ]