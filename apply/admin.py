from django.contrib import admin
from apply.models import Laborer, Operator
from marketing.models import AboutText, ServicesBlock1, ServicesBlock2

# Registering models pertaining to job applicants
admin.site.register(Laborer)
admin.site.register(Operator)

# Registering models that change the content displayed on the homepage
admin.site.register(AboutText)
admin.site.register(ServicesBlock1)
admin.site.register(ServicesBlock2)
