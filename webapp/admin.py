from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from webapp.models import *


# Register your models here.
admin.site.register(City)
admin.site.register(Currency)
admin.site.register(Product)
admin.site.register(Consumer)
