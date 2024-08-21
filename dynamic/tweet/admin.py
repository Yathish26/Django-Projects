from django.contrib import admin
from tweet.models import Tweet

# Register your models here.
class Tweetadmin(admin.ModelAdmin):
    list_display=('username','tweet','created_at')


admin.site.register(Tweet,Tweetadmin)