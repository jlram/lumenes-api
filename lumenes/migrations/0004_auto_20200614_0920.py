# Generated by Django 3.0.7 on 2020-06-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumenes', '0003_auto_20200613_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
