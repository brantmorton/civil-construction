from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from .forms import LaborerForm, OperatorForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from civil.settings import MEDIA_ROOT


class ApplyRoute(TemplateView):
    template_name = 'apply/apply-route.html'


def apply_laborer(request):
    if request.method == 'POST':
        form = LaborerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            data = request.POST.copy()
            subject = 'New applicant for the Laborer Position'
            context = {'first_name': data.get('first_name'),
                       'last_name': data.get('last_name'),
                       'email': data.get('email')}
            html_message = render_to_string('send/laborer_email.html', context)
            msg = EmailMessage(subject, html_message, 'brantmort@gmail.com', ['brantmort@gmail.com'])
            msg.content_subtype = "html"
            application_file_name = str(request.FILES['completed_application'].name).replace(' ', '_')
            try:
                resume_file_name = str(request.FILES.get('resume').name).replace(' ', '_')
                msg.attach_file(MEDIA_ROOT + resume_file_name)
            except AttributeError:
                pass
            msg.attach_file(MEDIA_ROOT + application_file_name)
            msg.send()
            messages.success(request, "Your application has been submitted!")
            return redirect('thank-you')
    else:
        form = LaborerForm()
    return render(request, 'apply/laborer_application.html', {'form': form})


def apply_operator(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted!")
            return redirect('home-page')
    else:
        form = OperatorForm()
    return render(request, 'apply/operator_application.html', {'form': form})
