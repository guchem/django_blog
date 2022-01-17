from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('logout',LogoutView.as_view(), name='logout'), 
    path('login',LoginView.as_view(template_name='accounts/login.html'), name='login')
]
