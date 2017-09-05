from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events),
    url(r'^user/new/$', views.user_new, name='user_new'),
]
