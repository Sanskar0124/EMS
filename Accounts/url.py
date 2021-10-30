from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('approve/<str:email>', views.approveEmp, name="approveEmp"),
    path('reject/', views.rejectEmp, name="rejectEmp"),
]