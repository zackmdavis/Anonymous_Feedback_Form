from django.conf.urls import include, url
from django.contrib import admin

from feedback.views import feedback_view

urlpatterns = [
    url(r'^anonymous-feedback/$', feedback_view, name='feedback')
]
