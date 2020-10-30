from django.urls import path

from Model3 import views

urlpatterns = [
    path('select.html/', views.select_html),
    path('import.html/', views.import_html),
    path('add/', views.add),
    path('select_for_update/', views.select_for_update),
    path('update/', views.update),
    path('delete/', views.delete),
    path('check_data/', views.check_data),
    path('import_data/', views.import_data),
]
