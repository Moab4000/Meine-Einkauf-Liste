from django.urls import path
from .views import KaufsListe, ListeDetail, ListeErstellung, ListeUpdate, DeleteView, CustomLoginView, RegisterPage, TeilenView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='einloggen'),
    path('logout/', LogoutView.as_view(next_page='einloggen'), name='ausloggen'),
    path('register/', RegisterPage.as_view(), name='registrieren'),

    path('', KaufsListe.as_view(), name='listen'),
    path('liste/<int:pk>/', ListeDetail.as_view(), name='liste'),
    path('liste-erstellung/', ListeErstellung.as_view(), name='liste-erstellung'),
    path('liste-update/<int:pk>/', ListeUpdate.as_view(), name='liste-update'),
    path('liste-delete/<int:pk>/', DeleteView.as_view(), name='liste-delete'),
    path('base/teilen.html/', TeilenView.as_view(), name='teilen'),
]