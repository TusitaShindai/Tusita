from django.urls import path
from tusitaapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),  # Example for an 'about' page
    path('gallery', views.gallery, name='gallery'), 
    path('inA', views.inA),  # Example for an 'inA' page
    path('AS', views.AS, name='AS'),
]
