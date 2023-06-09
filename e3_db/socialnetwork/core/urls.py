from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', views.profiles_list),
    path('profiles/<int:id>', views.profile_detail),
    path('connections/', views.connections_list),
    path('connection_recommendations/<int:id>', views.connection_recomendation)
]