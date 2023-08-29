from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_list_books),
    path('<int:pk>/', views.get_update_delete_book)
]
