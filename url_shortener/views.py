from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

import random
import short_url

from . import forms


class URLShortener(FormView):
    template_name = 'index.html'
    form_class = forms.URLForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        link = form.cleaned_data['url']
        self.success_url += f"?url={short_url.encode_url(random.randint(0, 100))}"
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        link_param = self.request.GET.get('url')
        if link_param:
            context['url'] = link_param
        return context