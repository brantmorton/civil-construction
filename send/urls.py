from django.urls import path, include
from send import views as send_views

urlpatterns = [
    path('thanks/', send_views.send_email, name='thank-you')
]