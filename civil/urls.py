"""civil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from marketing.views import HomePage
from apply import views as apply_views
from apply.views import ApplyRoute, ThankYouPage
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', ApplyRoute.as_view(), name='apply-route'),
    path('apply/laborer/', apply_views.apply_laborer, name='apply-laborer'),
    path('apply/operator/', apply_views.apply_operator, name='apply-operator'),
    path('', HomePage.as_view(), name='home-page'),
    path('thanks/', ThankYouPage.as_view(), name='thank-you'),

    # this is needed to utilize tinymce
    url(r'^tinymce/', include('tinymce.urls'))
]

# Media files in debug mode
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)