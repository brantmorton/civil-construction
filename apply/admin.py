from django.contrib import admin
from apply.models import Laborer, Operator
from marketing.models import AboutText, ServicesBlock1, ServicesBlock2

# Register your models here.
admin.site.register(Laborer)
admin.site.register(Operator)
admin.site.register(AboutText)
admin.site.register(ServicesBlock1)
admin.site.register(ServicesBlock2)
