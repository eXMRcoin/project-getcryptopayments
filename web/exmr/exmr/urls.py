"""exmr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from apps.common.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password-reset-done', PasswordResetDoneView.as_view(template_name='accounts/forgot_password_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('apps.accounts.urls')),
    # path('', TemplateView.as_view(template_name="common/index.html"), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='signin'),

    path('sign-up/', TemplateView.as_view(template_name='accounts/signup.html'),
         name='signup'),
    path('forgot-password/', TemplateView.as_view(template_name='accounts/forgot-password.html'), name='forgot-password'),
    path('accounts/', include('apps.accounts.urls')),


]

urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
