from django.urls import path

from Model8 import views

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
    # path('search_chejian_by_xianbie/', views.search_chejian_by_xianbie),
    # path('search_chezhan_by_chejian/', views.search_chezhan_by_chejian),
    path('search_fileds_by_quduan/', views.search_fileds_by_quduan),
    ]
