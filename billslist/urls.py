import urllib.parse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillsList

router = DefaultRouter()

urlpatterns = [
    path('api/v1/billslist/<int:page>/', BillsList.as_view(), name='billslist')
]
