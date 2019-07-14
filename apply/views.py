from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from .forms import LaborerForm, OperatorForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class ApplyRoute(TemplateView):
    template_name = 'apply/apply-route.html'


class ThankYouPage(TemplateView):
    template_name = 'apply/thank_you.html'


def apply_laborer(request):
    if request.method == 'POST':
        form = LaborerForm(request.POST, request.FILES)
        if form.is_valid():
            job_title = 'Laborer'
            send_email(request, form, job_title)
            return redirect('thank-you')
    else:
        form = LaborerForm()
    return render(request, 'apply/laborer_application.html', {'form': form})


def apply_operator(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST, request.FILES)
        if form.is_valid():
            job_title = 'Operator'
            send_email(request, form, job_title)
            return redirect('thank-you')
    else:
        form = OperatorForm()
    return render(request, 'apply/operator_application.html', {'form': form})


def send_email(request, form, job_title):
    data = request.POST.copy()
    subject = f'New applicant for the { job_title } Position'
    context = {'job_title': job_title,
               'first_name': data.get('first_name'),
               'last_name': data.get('last_name'),
               'email': data.get('email')}
    html_message = render_to_string('apply/laborer_email.html', context)
    msg = EmailMessage(subject, html_message, 'ccc.applicant.email@gmail.com', ['ccc.applicant.email@gmail.com'])
    msg.content_subtype = "html"
    if request.FILES:
        application_file = request.FILES.get('completed_application')
        msg.attach(application_file.name, application_file.read(), application_file.content_type)
        try:
            resume_file = request.FILES.get('resume')
            msg.attach(resume_file.name, resume_file.read(), resume_file.content_type)
        except AttributeError:
            pass
    msg.send()
    form.save()
    messages.success(request, "Your application has been submitted!")