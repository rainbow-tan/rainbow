from django.urls import path

from Model4 import views4

urlpatterns = [
    path('select.html/', views4.select_html),
    path('import.html/', views4.import_html),
    path('add/', views4.add),
    path('select_for_update/', views4.select_for_update),
    path('update/', views4.update),
    path('delete/', views4.delete),
    path('check_data/', views4.check_data),
    path('import_data/', views4.import_data),
    ]
