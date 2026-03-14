from django.urls import path
from .views import add_two_number
urlpatterns = [
    path('add/' , add_two_number)
]
