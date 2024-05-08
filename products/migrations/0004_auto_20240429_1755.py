# Generated by Django 3.2.25 on 2024-04-29 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20240423_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachingSession',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('date_time', models.DateTimeField()),
                ('topic', models.CharField(max_length=200)),
                ('coach', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='coaching_sessions',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
        migrations.RemoveField(
            model_name='series',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='series',
            name='categories',
            field=models.ManyToManyField(
                blank=True,
                related_name='series',
                to='products.Category'
            ),
        ),
        migrations.CreateModel(
            name='CoachingToken',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('price', models.DecimalField(
                    decimal_places=2,
                    max_digits=6
                )),
                ('identifier_code', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    unique=True
                )),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('is_used', models.BooleanField(default=False)),
                ('session', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='tokens',
                    to='products.coachingsession'
                )),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='tokens',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
    ]
