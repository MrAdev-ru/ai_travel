from django.urls import path
from . import views

app_name = 'translations'

urlpatterns = [
    path('', views.translate_view, name='translate'),
    path('history/', views.history_view, name='history'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('favorites/add/', views.add_favorite_view, name='add_favorite'),
    path('favorites/<int:pk>/remove/', views.remove_favorite_view, name='remove_favorite'),
    path('api/detect/', views.detect_language_view, name='detect_language'),
    path('api/translate/', views.ajax_translate_view, name='ajax_translate'),
]
