from django.contrib import admin

# Register your models here.
from .models import Language,Paradigm,Programmer

admin.site.register(Language)
admin.site.register(Paradigm)
admin.site.register(Programmer)
