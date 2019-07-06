from django.shortcuts import render


def send_email(request):
    template_name = 'send/thank_you.html'
    return render(request, template_name)




