from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(ServiceProvider)
admin.site.register(ServiceCategory)
admin.site.register(Item)
admin.site.register(Link)