from django.contrib import admin

# Из модуля models импортируем модель Tag...
from .models import Tag

# ...и регистрируем её в админке:
admin.site.register(Tag)
