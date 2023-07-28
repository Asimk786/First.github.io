from django.contrib import admin
from django.urls import path
from mainApp import view as mainApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homePage),
    path('about/',mainApp.aboutPage),
    path('profile/',mainApp.profilePage),
    path('contact/',mainApp.contactPage),
    
]
