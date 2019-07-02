from django.contrib import admin
from apply.models import Laborer, Operator
from marketing.models import AboutText

# Register your models here.
admin.site.register(Laborer)
admin.site.register(Operator)
admin.site.register(AboutText)