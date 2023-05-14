from . import views
from django.urls import path


urlpatterns = [
    path('subscribe/', views.subscribe, name = 'subscribe'),
    path('thank_you/,', views.thank_you, name='thank_you')
]
