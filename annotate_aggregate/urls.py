from django.urls import path

from . import views

app_name = "annotate_aggregate"

urlpatterns = [
    path('', views.index, name='index'),

]