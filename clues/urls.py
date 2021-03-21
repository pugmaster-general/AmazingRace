from django.urls import path
from . import views

app_name = 'clues'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:clue_id>/', views.detail, name='detail'),
]