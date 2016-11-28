# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .views import ModelListView, AdminListView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^models.py$', ModelListView.as_view(), name='models'),
    url(r'^admin.py$', AdminListView.as_view(), name='admin'),
]
