from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('create_folder/<int:parent_id>/', views.create_folder, name='create_folder_with_parent'),
    path('folders/', views.folder_list, name='folder_list'),
    path('folders/<int:folder_id>/', views.folder_list, name='subfolder_list'),

    path('api/folders/', api_views.folder_list_create, name='folder_list_create'),
    path('api/folders/<int:parent_id>/', api_views.folder_list_create, name='folder_list_create_with_parent'),
]
