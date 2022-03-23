# Generated by Django 4.0.3 on 2022-03-15 16:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs_app', '0009_rename_performance_by_song_performed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='reviewers',
            field=models.ManyToManyField(through='songs_app.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
