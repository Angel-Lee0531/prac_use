
from django.contrib import admin
from django.urls import path
from text import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('count/', views.count, name="countnickname")
]
