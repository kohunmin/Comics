__author__ = 'haegyun'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<book_id>[0-9]+)$', views.detail, name='detail'),
]