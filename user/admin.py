from django.contrib import admin
from user.models import User, UniqueRegistration
admin.site.register(User)
admin.site.register(UniqueRegistration)


