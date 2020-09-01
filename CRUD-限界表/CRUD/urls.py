from django.contrib import admin
from django.urls import path

from Model import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_html),
    path('login.html/', views.login_html),
    path('index.html/', views.index_html),
    path('select.html/', views.select_html),
    path('import.html/', views.import_html),
    path('login/', views.login),
    path('add/', views.add),
    path('select_for_update/', views.select_for_update),
    path('update/', views.update),
    path('delete/', views.delete),
    path('check_file/', views.check_data),
    path('import_data/', views.import_data),
    path('debug/', views.debug),

]

