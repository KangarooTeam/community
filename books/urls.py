from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_new'),
    path('book/<int:pk>/edit/',
        views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/',
        views.BookDeleteView.as_view(), name='book_delete'),
]