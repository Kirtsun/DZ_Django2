from django.urls import path

from . import views

app_name = "annotate_aggregate"

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/book/<int:pk>/', views.store_in, name='store_in'),
    path('authors/', views.authors, name='authors'),
    path('authors/books/<int:pk>/', views.authors_in, name='authors_in'),
    path('book/', views.book, name='book'),
    path('book/info/<int:pk>/', views.book_in, name='book_in'),
    path('publisher/', views.publisher, name='publisher'),


]
