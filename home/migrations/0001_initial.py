# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-08 00:35
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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('test', models.TextField()),
                ('collaboration', models.IntegerField(choices=[(0, 'private'), (1, 'shared'), (2, 'users')], default=0)),
                ('visibility', models.IntegerField(choices=[(0, 'private'), (1, 'shared'), (2, 'users'), (3, 'public')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('file', models.FileField(blank=True, upload_to='uploads/')),
                ('genre', models.CharField(max_length=30)),
                ('tags', models.CharField(max_length=120)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='home.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='collaborators',
            field=models.ManyToManyField(to='home.Profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='playlists',
            field=models.ManyToManyField(to='home.Playlist'),
        ),
        migrations.AddField(
            model_name='post',
            name='songs',
            field=models.ManyToManyField(to='home.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='collaborators',
            field=models.ManyToManyField(to='home.Profile'),
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
