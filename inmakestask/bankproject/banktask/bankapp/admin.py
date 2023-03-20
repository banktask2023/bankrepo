from django.contrib import admin
from .models import district,city,User

# Register your models here.
admin.site.register(district)
admin.site.register(city)
admin.site.register(User)