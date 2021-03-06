"""Importing views to assign functions to urls"""
from django.urls import path
from . import views

"""Write urls with the parameters in the url: string of character or numerical ID"""
urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('Legal_notice', views.Legal_notice, name="Legal_Notice"),
    path('results/<str:parse>/<str:name_categorie>/', views.results, name="results"),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('accueil', views.accueil, name="accueil"),
    path('', views.base, name="base"),
    path('register', views.register, name="register"),
    path('espace', views.espace, name="espace"),
    path('user_products', views.user_products, name="user_products"),
    path('details/<int:id>/', views.details, name="details"),
    path('save/<int:pk>/', views.save, name="save"),
]
