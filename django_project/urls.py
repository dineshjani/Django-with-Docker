

from django.urls import path
from api_response import response_api
urlpatterns = [
    path('', response_api),
]
