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
    """
    Given a POST method to the Laborer Form:
        - Verify that the data submitted is valid
        - Call send_email() to send an email with posted data and job title to HR
        - Returns a redirect to the "thank you" page

    Given a GET method:
        - Returns the Laborer application template
    """
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
    """
    Given a POST method to the Operator Form:
        - Verify that the data submitted is valid
        - Call send_email() to send an email with posted data and job title to HR
        - Returns a redirect to the "thank you" page

    Given a GET method:
        - Returns the Operator application template
    """
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
    """
    When called, will generate and send an email with all posted data along with
    the job applied for in an email to the HR Department

    This will also attach the files submitted in the application form.

    Note, an applicant's "resume" is not required, therefore a try/except
    was used to attach the file if available.
    """

    # this captures the post data that will be passed to the email template
    data = request.POST.copy()
    subject = f'New applicant for the { job_title } Position'
    context = {'job_title': job_title,
               'first_name': data.get('first_name'),
               'last_name': data.get('last_name'),
               'email': data.get('email')}

    # this is rendering the data submitted to an html formatted email template
    html_message = render_to_string('apply/laborer_email.html', context)
    msg = EmailMessage(subject, html_message, 'ccc.applicant.email@gmail.com', ['shane@cccesi.com'])
    msg.content_subtype = "html"

    # this block handles files attached to the completed application
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