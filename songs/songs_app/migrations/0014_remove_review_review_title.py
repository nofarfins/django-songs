# Generated by Django 4.0.3 on 2022-04-07 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0013_alter_performance_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_title',
        ),
    ]
