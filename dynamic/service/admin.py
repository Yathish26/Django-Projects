from django.contrib import admin
from .models import Blogs

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('Title','Category','Description','Photos')
    
admin.site.register(Blogs,BlogAdmin)