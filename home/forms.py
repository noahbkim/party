from django import forms
from . import models


class TagForm(forms.ModelForm):

    class Meta:
        model = models.Tag
        fields = ["name"]


class SongForm(forms.ModelForm):

    def is_valid(self):
        return True

    class Meta:
        model = models.Song
        fields = ["title", "artist", "remixer", "url", "file", "genre", "tags"]
