
from django.contrib import admin
from django.urls import path
from dataApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/',views.UserApi)
]
