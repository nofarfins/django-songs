# Generated by Django 4.0.3 on 2022-03-15 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0007_remove_performance_reviewers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='singer',
            new_name='Performance_by',
        ),
    ]
