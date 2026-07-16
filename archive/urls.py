from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('levels/', views.levels_list, name='levels_list'),
    path('level/<int:level_id>/', views.level_detail, name='level_detail'),
]