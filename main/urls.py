from django.urls import path

from . import views

urlpatterns  = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("lostSouls/", views.lostSouls, name="Cave of Lost Souls"),
path("havlin/", views.havlin, name="Havlin"),
]