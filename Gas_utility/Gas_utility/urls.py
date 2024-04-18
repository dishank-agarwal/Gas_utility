from django.contrib import admin
from django.urls import path, include
from Gas_Services import views as gas_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gas_services/', include('Gas_Services.urls')),
    path('', gas_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/login/', gas_views.custom_login, name='login'),
]
