# Generated by Django 3.2.25 on 2024-05-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_image',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
