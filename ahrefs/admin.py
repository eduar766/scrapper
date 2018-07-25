from django.contrib import admin
from .models import UrlSearch, Backlinks, TokenAhref

# Register your models here.
admin.site.register(UrlSearch)
admin.site.register(Backlinks)
admin.site.register(TokenAhref)
