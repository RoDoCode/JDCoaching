# Generated by Django 3.2.25 on 2024-05-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_series_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='screenshot',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
