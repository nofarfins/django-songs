# Generated by Django 4.0.3 on 2022-03-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0006_performance_reviewers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='reviewers',
        ),
    ]
