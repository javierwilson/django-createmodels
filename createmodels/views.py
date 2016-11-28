# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Model, Field


class ModelDetailView(LoginRequiredMixin, DetailView):
    model = Model


class ModelListView(LoginRequiredMixin, ListView):
    model = Model
    content_type='text/plain; charset=utf8'


class AdminListView(LoginRequiredMixin, ListView):
    model = Model
    template_name = 'createmodels/admin_list.html'
    content_type='text/plain; charset=utf8'
