from django.urls import path

from . import views

app_name = "annotate_aggregate"

urlpatterns = [
    path('', views.index, name='index'),
    path('store_book/<int:pk>/', views.store_book, name='store_book'),
    path('book/<int:pk>/', views.book, name='book'),
    path('publisher/<int:pk>/', views.publisher, name='publisher')

]
