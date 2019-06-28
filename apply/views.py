from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from .forms import LaborerForm, OperatorForm


class ApplyRoute(TemplateView):
    template_name = 'apply/apply-route.html'


def apply_laborer(request):
    if request.method == 'POST':
        form = LaborerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted!")
            return redirect('home-page')
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
