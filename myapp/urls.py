from django.urls import path
from . import views
from .views import CreateUserView

urlpatterns = [
    path('', views.user_manager, name='user_manager'),
    path('users/', views.user_manager, name='user_manager'),
    path('crear-usuario/', CreateUserView.as_view(), name='crear_usuario'),
    path('about', views.about, name="about"),
]
