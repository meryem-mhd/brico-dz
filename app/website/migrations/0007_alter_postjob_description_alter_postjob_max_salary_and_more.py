# Generated by Django 4.1 on 2022-08-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_delete_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjob',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='postjob',
            name='max_salary',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='postjob',
            name='min_salary',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
