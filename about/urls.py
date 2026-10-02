from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('dormitory/', views.dormitory_detail, name='dormitory'),
    path('block/<int:pk>/', views.block_detail, name='block'),
]
