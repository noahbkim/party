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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Song(models.Model):
    """A song upload container."""

    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    remixer = models.CharField(max_length=60)

    url = models.CharField(max_length=120)
    file = models.FileField(upload_to="uploads/", blank=True)

    genre = models.CharField(max_length=30)
    tags = models.CharField(max_length=120)

    uploader = models.ForeignKey(Profile, related_name="uploads")
    upload_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def upload_path(self):
        """Generate an upload path."""

        name = "{} - {}".format(self.artist, self.title)
        if self.remixer:
            name += " ({} remix)".format(self.remixer)
        return name


class Playlist(models.Model):
    """A playlist model."""

    title = models.CharField(max_length=60)
    creator = models.ForeignKey(Profile, related_name="playlists")
    songs = models.ManyToManyField(Song)

    collaboration = models.IntegerField(choices=COLLABORATION_LEVELS, default=0)
    collaborators = models.ManyToManyField(Profile)
    visibility = models.IntegerField(choices=VISIBILITY_LEVELS, default=0)


class Post(models.Model):
    """A blog type post."""

    title = models.CharField(max_length=60)
    test = models.TextField()
    songs = models.ManyToManyField(Song)
    playlists = models.ManyToManyField(Playlist)
    author = models.ForeignKey(User)

    collaboration = models.IntegerField(choices=COLLABORATION_LEVELS, default=0)
    collaborators = models.ManyToManyField(Profile)
    visibility = models.IntegerField(choices=VISIBILITY_LEVELS, default=0)
