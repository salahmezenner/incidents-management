from django.contrib import admin
from .models import Incident,Platform,Profile,CelluleDeCrise

# Register your models here.
admin.site.register(Incident)
admin.site.register(Platform)
admin.site.register(Profile)
admin.site.register(CelluleDeCrise)