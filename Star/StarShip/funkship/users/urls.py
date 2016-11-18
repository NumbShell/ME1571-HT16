from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registered/$', views.users, name='users'),
    url(r'^browser/$', views.browser, name='browser'),
    url(r'^detail/$', views.detail, name='detail'),
]