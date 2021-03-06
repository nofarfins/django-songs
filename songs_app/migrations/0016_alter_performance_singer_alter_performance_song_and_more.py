# Generated by Django 4.0.3 on 2022-04-12 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs_app', '0015_remove_song_performed_by_alter_review_performance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs_app.artist'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs_app.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_composer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='composer', to='songs_app.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='songs_app.artist'),
        ),
    ]
