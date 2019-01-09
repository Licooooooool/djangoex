from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^1/',views.bar_zome),
    url(r'^4/',views.line3d),
    url(r'^2/',views.pie),
    url(r'^3/',views.polar),
]