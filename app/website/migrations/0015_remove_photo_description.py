# Generated by Django 4.1 on 2022-09-13 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_project_remove_photo_category_alter_photo_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
    ]
