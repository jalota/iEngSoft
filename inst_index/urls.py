from django.urls import path
from . import views

app_name = 'inst_index'

urlpatterns = [
    path('view/', views.view_index, name="view"),
]
