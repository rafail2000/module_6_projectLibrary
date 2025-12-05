from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('books_list/', views.books_list, name='books_list'),
    path('books_detail/<int:book_id>', views.book_detail, name='books_detail')
]