# Generated by Django 4.0.3 on 2022-03-10 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('information', models.CharField(max_length=4256)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_of_views', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('information', models.CharField(max_length=4256)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('information', models.CharField(max_length=4256)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('lyrics', models.CharField(max_length=4256)),
                ('song_composer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='songs_app.composer')),
                ('song_writer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='songs_app.writer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=128)),
                ('review_text', models.CharField(max_length=512)),
                ('Performance_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='songs_app.performance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='performance',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='songs_app.singer'),
        ),
        migrations.AddField(
            model_name='performance',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='songs_app.song'),
        ),
    ]
