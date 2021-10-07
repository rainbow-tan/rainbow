from django.urls import path

from Model5 import views

urlpatterns = [
    path('select.html/', views.select_html),
    path('add.html/', views.add_html),
    path('update.html/', views.update_html),
    path('update/', views.update),
    path('add/', views.add),
    path('delete/', views.delete),
    path('search_chejian/', views.search_chejian),
    path('search_chezhan/', views.search_chezhan),
    path('search_fenlei/', views.search_fenlei),
    path('search_renwuliang_danwei/', views.search_renwuliang_danwei),
    path('zhuye.html/', views.zhuye_html),
    path('zhuye/', views.zhuye),
    path('history.html/', views.history_html),
    path('import.html/', views.import_html),
    path('see_data/', views.see_data),
    path('import_data/', views.import_data),
    path('history_add.html/', views.history_add_html),
    ]
