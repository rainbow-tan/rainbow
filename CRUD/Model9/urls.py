from django.urls import path

from Model9 import views

urlpatterns = [
    path('select.html/', views.select_html),
    path('import.html/', views.import_html),
    path('add.html/', views.add_html),
    path('add/', views.add),
    path('update.html/', views.update_html),
    path('update/', views.update),
    path('delete/', views.delete),
    path('check_data/', views.check_data),
    path('import_data/', views.import_data),
    ]
