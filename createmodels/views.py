# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Model, Field


class ModelDetailView(LoginRequiredMixin, DetailView):
    model = Model


class ModelListView(ListView):
    model = Model
    content_type='text/plain; charset=utf8'


class AdminListView(ListView):
    model = Model
    template_name = 'createmodels/admin_list.html'
    content_type='text/plain; charset=utf8'


    def get_context_data(self, **kwargs):
        context = super(AdminListView, self).get_context_data(**kwargs)
        context['inlines'] = Model.inlines.through.objects.all()
        return context
