from django.contrib import admin
from django.urls import path

from Model import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.select_html),
    path('login.html/', views.login_html),
    path('select.html/', views.select_html),
    path('add.html/', views.add_html),
    path('add/', views.add),
    path('update.html/', views.update_html),
    path('update/', views.update),
    path('delete/', views.delete),
    path('to_lead.html/', views.to_lead_html),
    path('upload/', views.upload),
    path('choose_select.html/', views.choose_select_html),
    path('choose_select/', views.choose_select),
    path('debug/', views.debug),

]
