from django.urls import path

from ModelA import views

urlpatterns = [
    path('update.html/', views.update_html),
    path('setting.html/', views.setting_html),
    path('update/', views.update),
    path('update6/', views.update6),
    ]
