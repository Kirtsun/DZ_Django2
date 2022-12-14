from django.urls import path

from . import views

app_name = "annotate_aggregate"

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/book/<int:pk>/', views.store_in, name='store_in'),
    path('authors/', views.authors, name='authors'),
    path('authors/books/<int:pk>/', views.authors_in, name='authors_in'),

    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('books/', views.BookList.as_view(), name='books-list'),

    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),

    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher-create'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),

    path('publisher/<int:pk>/update/', views.PublisherUpdate.as_view(), name='publisher-update'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),

    path('publisher/<int:pk>/delete', views.PublisherDelete.as_view(), name='publisher-delete'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

    path('contact_form/', views.contact_form, name='contact_form'),

]
