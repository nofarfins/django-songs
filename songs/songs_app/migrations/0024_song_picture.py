# Generated by Django 4.0.3 on 2022-04-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0023_alter_artist_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='picture',
            field=models.URLField(blank=True, max_length=4256, null=True),
        ),
    ]