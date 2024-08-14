from django.contrib import admin
from . models import Platform , Incident , Profile , CelluleDeCrise , Event , Couche

admin.site.register(Platform)
admin.site.register(Incident)
admin.site.register(Profile)
admin.site.register(CelluleDeCrise)
admin.site.register(Event)
admin.site.register(Couche)