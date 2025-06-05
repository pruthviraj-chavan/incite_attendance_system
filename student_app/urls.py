from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request_attendance/', views.request_attendance, name='request_attendance'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve_attendance/<int:request_id>/', views.approve_attendance, name='approve_attendance'),
    path('reject_attendance/<int:request_id>/', views.reject_attendance, name='reject_attendance'),
    path('update_fee_status/<int:fee_id>/', views.update_fee_status, name='update_fee_status'),
    path('courses/', views.courses_page, name='courses'),
    path('ai-tools/', views.ai_tools_page, name='ai_tools'),
    path('resources/', views.resources_page, name='resources')
]