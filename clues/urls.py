from django.urls import path
from . import views

app_name = 'clues'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:clue_id>/', views.detail, name='detail'),
    path('volleyball/', views.VolleyballLeaderboard.as_view(), name='volleyball'),
    path('jenga/', views.JengaLeaderboard.as_view(), name='jenga'),
    path('update-volleyball/', views.update_volleyball, name="update-volleyball"),
    path('update-jenga/', views.update_jenga, name="update-jenga"),
]