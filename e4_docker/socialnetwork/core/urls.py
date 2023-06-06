from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'core/index.html')),
    path('admin/', admin.site.urls),
    path('profiles/', views.profiles_list),
    path('profiles/<int:id>', views.profile_detail),
    path('connections/', views.connections_list),
    path('connection_recommendations/<int:id>', views.connection_recomendation)
]