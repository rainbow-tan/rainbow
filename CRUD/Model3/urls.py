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
    path('select_changdu_by_guidao/', views.select_changdu_by_guidao),
    path('gcdpldfx/', views.gcdpldfx),
    path('gcdpfxld/', views.gcdpfxld),
    path('jsdpldfx/', views.jsdpldfx),
    path('jsdpfxld/', views.jsdpfxld),
    path('network_length_7/', views.network_length_7),
    path('reality_length_7/', views.reality_length_7),
    path('compensation_7/', views.compensation_7),

    path('network_length_10/', views.network_length_10),
    path('reality_length_10/', views.reality_length_10),
    path('compensation_10/', views.compensation_10),
    ]
