from django.contrib import admin
from django.urls import path, include
from .views import show_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first', show_list),
    path('lab/', include('website.urls')),
]
