from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


COLLABORATION_LEVELS = (
    (0, "private"),
    (1, "shared"),
    (2, "users")
)

VISIBILITY_LEVELS = (
    (0, "private"),
    (1, "shared"),
    (2, "users"),
    (3, "public")
)


class Profile(models.Model):
    """User profile."""

    user = models.OneToOneField(User, related_name="profile")
    #avatar = models.ImageField()
    #status = models.TextField()

    @staticmethod
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @staticmethod
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Tag(models.Model):
    """A concise description of a song."""

    name = models.CharField(max_length=20)


class Song(models.Model):
    """A song upload container."""

    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    remixer = models.CharField(max_length=60)
    url = models.CharField(max_length=120)

    genre = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag)

    uploader = models.ForeignKey(Profile, related_name="uploads")
    upload_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)


class Playlist(models.Model):
    """A playlist model."""

    title = models.CharField(max_length=60)
    creator = models.ForeignKey(Profile, related_name="playlists")
    songs = models.ManyToManyField(Song)

    collaboration = models.IntegerField(choices=COLLABORATION_LEVELS, default=0)
    collaborators = models.ManyToManyField(Profile, related_name="playlists_shared")
    visibility = models.IntegerField(choices=VISIBILITY_LEVELS, default=0)
