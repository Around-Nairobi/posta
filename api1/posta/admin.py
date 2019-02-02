from django.contrib import admin
from .models import errors

# Register your models here.
myModels = [errors]
admin.site.register(myModels)
