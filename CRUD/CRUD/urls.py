from django.contrib import admin
from django.urls import include
from django.urls import path

from CRUD import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_html),
    path('login.html/', views.login_html),
    path('index.html/', views.index_html),
    path('debug.html/', views.debug_html),
    path('debug/', views.debug),
    path('login/', views.login),

    path('Model/', include('Model.urls')),
    path('Model2/', include('Model2.urls')),
    path('Model3/', include('Model3.urls')),
    path('Model4/', include('Model4.urls')),
    path('Model5/', include('Model5.urls')),
    path('Model6/', include('Model6.urls')),
    path('Model7/', include('Model7.urls')),
    path('Model8/', include('Model8.urls')),
    path('Model9/', include('Model9.urls')),
    path('ModelA/', include('ModelA.urls')),
    ]
