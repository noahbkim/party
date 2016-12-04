# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-03 16:01
from __future__ import unicode_literals

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
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('collaboration', models.IntegerField(choices=[(0, 'private'), (1, 'shared'), (2, 'users')], default=0)),
                ('visibility', models.IntegerField(choices=[(0, 'private'), (1, 'shared'), (2, 'users'), (3, 'public')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('artist', models.CharField(max_length=60)),
                ('remixer', models.CharField(max_length=60)),
                ('url', models.CharField(max_length=120)),
                ('genre', models.CharField(max_length=30)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='tags',
            field=models.ManyToManyField(to='home.Tag'),
        ),
        migrations.AddField(
            model_name='song',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='home.Profile'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='collaborators',
            field=models.ManyToManyField(related_name='playlists_shared', to='home.Profile'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='home.Profile'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='home.Song'),
        ),
    ]