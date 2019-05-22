from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted!")
            return redirect('home-page')
    else:
        form = ApplicationForm()
    return render(request, 'apply/application_page.html', {'form': form})
