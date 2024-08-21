from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_description','news_image','news_category')

    
admin.site.register(News,NewsAdmin)