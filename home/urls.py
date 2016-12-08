from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^about/$", views.about, name="about"),
    url(r"^home/$", views.home, name="home"),
    url(r"^home/posts/$", views.posts, name="home"),
    url(r"^home/library/$", views.library, name="home"),
    url(r"^home/library/upload/", views.library_upload, name="home"),
    url(r"^home/playlists/", views.playlists, name="home"),
    url(r"^home/users/", views.users, name="home"),
    url(r"^login", views.login, name="login"),
    url(r"^logout", views.logout, name="logout")
]
