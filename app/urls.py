from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from cars import views
from users.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('', views.CarListView.as_view(), name='home'),
    path('cars/list/', views.CarListView.as_view(), name='car_list'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/detail/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
]
