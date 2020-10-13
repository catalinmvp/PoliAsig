from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import PhysicalCustomer,Company
admin.site.register(Company)
admin.site.register(PhysicalCustomer)