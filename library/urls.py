from django.urls import path
# from . import views
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView

app_name = 'library'

urlpatterns = [
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]