# Generated by Django 4.2 on 2023-04-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique_for_date='publish'),
        ),
    ]
