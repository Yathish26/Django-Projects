from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #admin setup unitll here
    path('', views.home),
    path('home/', views.homedirect),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
    path('userform/',views.userform),
    path('calculator/',views.calculator),
    path('random/<content>',views.random),
    path('evenodd/',views.evenodd),
    path('marksheet/',views.marksheet),
    path('blogs/',views.blogs),
    path("blogs/create-blog",views.blogcreate,name='blogged'),
    path("blogs/content/<blogdetail>", views.blogdetail),
    #news subparts below
    path("news/", views.news),
    path("news/create",views.newscreate,name='newsupdate'),
    path("news/content/<maq>",views.newsdetails),
    path("news/topnews",views.topnews),
    path("news/agriculture",views.agriculture),
    path("news/automobiles", views.automobiles),
    path("news/business", views.business),
    path("news/crime", views.crime),
    path("news/education", views.education),
    path("news/entertainment", views.entertainment),
    path("news/health", views.health),
    path("news/lifestyle", views.lifestyle),
    path("news/politics", views.politics),
    path("news/science", views.science),
    path("news/sports", views.sports),
    path("news/technology", views.technology),
    path('tweets/',views.tweet,name='tweeted'),

]   

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)