# Generated by Django 3.1.1 on 2020-09-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billslist', '0003_auto_20200929_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='image_url',
            new_name='original_url',
        ),
        migrations.AddField(
            model_name='bill',
            name='thumbnail_url',
            field=models.TextField(default='https://via.placeholder.com/120'),
        ),
    ]
