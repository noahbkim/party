from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from . import models
from . import forms


def index(request):
    if not request.user.is_anonymous and request.user.is_authenticated:
        return redirect("/home")
    return render(request, "home/index.html", {})


def about(request):
    pass


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return redirect("/login?invalid=1")
        auth.login(request, user)
        return redirect("/home")

    return render(request, "home/login.html")


@login_required(login_url="/login")
def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required(login_url="/login")
def home(request):
    return render(request, "home/home.html")


@login_required()
def posts(request):
    return render(request, "home/posts.html")


@login_required()
def library(request):

    count = request.GET.get("count")
    if count is None or not count.isnumeric() and count != "all":
        count = 50
    else:
        count = int(count)

    page = request.GET.get("page")
    if page is None or not page.isnumeric() or count == "all":
        page = 1
    else:
        page = int(page)

    songs = []
    if count != "all":
        paginator = Paginator(models.Song.objects.all(), count)
        songs = paginator.page(page).object_list
    else:
        songs = models.Song.objects.all()

    return render(request, "home/library.html", {"songs": songs})


@login_required()
def library_upload(request):

    if "edit" in request.GET:
        return library_edit(request)

    if request.method == "POST":
        form = forms.SongForm(request.POST)
        song = form.save(commit=False)
        song.uploader = request.user.profile
        song.save()
        return redirect("/home/library")

    form = forms.SongForm()
    return render(request, "home/library_upload.html", {"form": form})


def library_edit(request):

    if not request.GET["edit"].isnumeric():
        return redirect("/home/library")

    id = int(request.GET["edit"])
    existing = models.Song.objects.filter(id=id).first()

    if request.method == "POST":
        form = forms.SongForm(request.POST, instance=existing)
        form.save()
        return redirect("/home/library")

    form = forms.SongForm(instance=existing)
    return render(request, "home/library_upload.html", {"form": form, "edit": "?edit=" + str(id)})


@login_required()
def playlists(request):
    return render(request, "home/playlists.html")


@login_required()
def users(request):
    return render(request, "home/users.html")
