# Generated by Django 4.0.3 on 2022-09-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_remove_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_experience',
            name='main_job',
            field=models.CharField(blank=True, choices=[('Paint', 'Paint'), ('Electricity', 'Electricity'), ('Plumbing', 'Plumbing'), ('Masonry', 'Masonry'), ('Industriel automation', 'Industriel automation'), ('Web developer', 'Web developer'), ('truck driver', 'truck driver')], default=None, max_length=100, null=True),
        ),
    ]
