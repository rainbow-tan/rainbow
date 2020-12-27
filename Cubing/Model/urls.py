from django.urls import path

from Model import views

urlpatterns = [
    path('select.html/', views.select_html),
    path('import.html/', views.import_html),
    path('add/', views.add),
    path('select_for_update/', views.select_for_update),
    path('select_for_auto_input/', views.select_for_auto_input),
    path('baofei.html/', views.baofei_html),
    path('update/', views.update),
    path('delete/', views.delete),
    path('scrap/', views.scrap),
    path('barcode/', views.barcode),
    path('max_barcode/', views.max_barcode),

    ]
