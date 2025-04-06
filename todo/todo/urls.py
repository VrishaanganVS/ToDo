from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('',views.signup),
    path('admin/',admin.site.urls),
]
