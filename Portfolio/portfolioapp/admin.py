from django.contrib import admin
from portfolioapp.models import Education, Experience
# from portfolioapp.models import * --> yesto gare, models.py ma bhayeko sabai classes import hunxa


# Register your models here.

admin.site.register(Education)
admin.site.register(Experience)

