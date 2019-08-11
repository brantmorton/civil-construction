from django.views.generic.base import TemplateView
from marketing.models import AboutText, ServicesBlock1, ServicesBlock2
from django.shortcuts import render, redirect


class HomePage(TemplateView):
    template_name = 'marketing/home.html'

    def get(self, request):
        """

        Given a GET method to the home page, this will load in
        the tinymce models that display the "about" and "services"
        sections to the home page template.

        """
        abouttext = AboutText.objects.get(id=1)
        servicesblock1 = ServicesBlock1.objects.get(id=1)
        servicesblock2 = ServicesBlock2.objects.get(id=1)

        args = {'abouttext': abouttext,
                'servicesblock1': servicesblock1,
                'servicesblock2': servicesblock2}

        return render(request, self.template_name, args)


