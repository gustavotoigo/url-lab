
from django.urls import path, include
from .views import list_error

urlpatterns = [
    path('', list_error),

]
