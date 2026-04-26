from django.contrib import admin
from .models import Publisher, Studio, Game

# تسجيل الجداول عشان تظهر في لوحة التحكم
admin.site.register(Publisher)
admin.site.register(Studio)
admin.site.register(Game)
# Register your models here.
