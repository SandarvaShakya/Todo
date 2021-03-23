from django.urls import path
from todolist.views import delete, index, completed

urlpatterns = [
    path('', index, name='index'),
    path('completed/<int:primary_key>/', completed, name='completed'),
    path('delete/<int:primary_key>/', delete, name='delete'),
]
