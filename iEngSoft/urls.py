from django.contrib import admin
from django.urls import path, include
from inst_index import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('inst_index/', include('inst_index.urls')),
]
