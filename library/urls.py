from django.urls import path
# from . import views
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView, AuthorCreateView, \
    AuthorUpdateView, AuthorListView, RecommendBookView, ReviewBookView

app_name = 'library'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:pk>/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
]