from django.contrib import admin

# Register your models here.
from .models import Bb

class BdAdmin (admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BdAdmin)