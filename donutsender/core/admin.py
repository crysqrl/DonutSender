from django.contrib import admin

from donutsender.core.models import User, Payment

admin.site.register(User)
admin.site.register(Payment)
