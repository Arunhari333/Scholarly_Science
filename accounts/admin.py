from django.contrib import admin
from accounts.models import register, detail

# Register your models here.
admin.site.register(register)
admin.site.register(detail)