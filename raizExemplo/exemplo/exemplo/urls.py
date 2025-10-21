"""
URL configuration for exemplo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from exemplo import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

urlpatterns = [
    path("admin/", 
        admin.site.urls, 
        name='admin'),
    path("contatos/", 
        include('contatos.urls')),
    #path("", include('contatos.urls')),
    path("", 
        views.home, 
        name="home"), 
    path("seguranca/", 
        views.homeSec, 
        name="homeSec"),
    path("seguranca/registro", 
        views.registro, 
        name="registroSec"),
    path("seguranca/login/", LoginView.as_view(template_name='seguranca/login.html'), name='loginSec'),
    path("accounts/login/", LoginView.as_view(template_name='seguranca/login.html')), # Redireciona para login se não autenticado
    path("seguranca/pagSec", views.pagSecreta, name="pagSecretaSec"),
    path("meuLogout/", views.logout, name="meuLogoutSec"), # Confirmar logout
    path("seguranca/logut", LogoutView.as_view(next_page=reverse_lazy('homeSec')), name='logoutSec'), # Link para efetuar logout
    path("seguranca/passwordChange/", 
        PasswordChangeView.as_view(template_name='seguranca/passwordChangeForm.html', 
                                    success_url=reverse_lazy('passwordChangeDoneSec')), 
        name='passwordChangeSec'
    ),
    path("seguranca/passwordChangeDone/", 
        PasswordChangeDoneView.as_view(template_name='seguranca/passwordChangeDone.html'), 
        name='passwordChangeDoneSec'
    ),
    path("seguraca/editarPerfil/<int:pk>/",
        UpdateView.as_view(template_name='seguranca/userForm.html',
                          model=User,
                          fields=['first_name', 'last_name', 'email'],
                          success_url=reverse_lazy('homeSec')
        ),
        name='editarPerfilSec'
    ),
    path('seguranca/password_reset/', 
        PasswordResetView.as_view(template_name='seguranca/passwordResetForm.html',
                                success_url=reverse_lazy('password_reset_done'),
                                html_email_template_name='seguranca/passwordResetEmail.html',
                                subject_template_name='seguranca/passwordResetSubject.txt',
                                from_email='webmaster@meslin.com.br',
        ),
        name='password_reset'
    ),
    path('seguranca/password_reset_done/', 
        PasswordResetDoneView.as_view(template_name='seguranca/passwordResetDone.html',),
        name='password_reset_done'
    ),
    path('seguranca/password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='seguranca/passwordResetConfirm.html',
                                        success_url=reverse_lazy('password_reset_complete'),
        ), 
        name='password_reset_confirm'
    ),
    path('seguranca/password_reset_complete/',
        PasswordResetCompleteView.as_view(template_name='seguranca/passwordResetComplete.html'), 
        name='password_reset_complete'
    ),
    path('exemplosback/',
        include('exemplosback.urls')
    ),
    path('carros/',
        include('carros.urls')
    ),
]
