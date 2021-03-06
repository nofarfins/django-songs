# Generated by Django 4.0.3 on 2022-03-10 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('songs_app', '0005_remove_performance_reviewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='reviewers',
            field=models.ManyToManyField(through='songs_app.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
