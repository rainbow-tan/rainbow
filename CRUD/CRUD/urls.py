from django.contrib import admin
from django.urls import path, include

from CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_html),
    path('login.html/', views.login_html),
    path('index.html/', views.index_html),
    path('debug.html/', views.debug_html),
    path('debug/', views.debug),
    path('login/', views.login),

    path('one/', include('Model.urls')),
    path('two/', include('Model2.urls')),
    path('three/', include('Model3.urls')),
    path('four/', include('Model4.urls')),
]
