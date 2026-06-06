from django.urls import path
from . import views

app_name = 'phrasebook'

urlpatterns = [
    path('', views.phrasebook_home, name='home'),
    path('<slug:slug>/', views.category_detail, name='category'),
]
