from django.urls import path
from . import views

urlpatterns = [
    # path('', views.book_list),
    path('', views.BookList.as_view()),
    path('save/', views.BookCreate.as_view()),
    # path('save/', views.book_create),
    # path('<str:pk>/', views.book),
    path('<str:pk>/', views.BookSingle.as_view()),
]       