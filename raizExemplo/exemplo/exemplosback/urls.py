from django.urls import path
from exemplosback import views
app_name ='exemplosback'
urlpatterns = [
    path('exemploClasse/', views.ExemploClasse.as_view(), name='exemploClasse'),
    path('exemploGET/', views.exemploGET, name='exemploGET'),
    path('exemploPOST/', views.exemploPOST, name='exemploPOST'),
    path('exemploPUTDELETE/', views.exemploPUTDELETE, name='exemploPUTDELETE'),
]