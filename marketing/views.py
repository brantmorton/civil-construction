from django.views.generic.base import TemplateView
from marketing.models import AboutText
from django.shortcuts import render, redirect
from tinymce.widgets import TinyMCE


class HomePage(TemplateView):
    template_name = 'marketing/home.html'

    def get(self, request):
        abouttext = AboutText.objects.get(id=1)

        args = {'abouttext': abouttext}

        return render(request, self.template_name, args)
