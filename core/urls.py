from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('servicos/', views.services, name='services'),
    path('servicos/<slug:slug>/', views.service_detail, name='service_detail'),
    path('galeria/', views.gallery, name='gallery'),
    path('contato/', views.contact, name='contact'),
    path('agendamento/horarios/', views.appointment_slots, name='appointment_slots'),
    path('agendamento/', views.appointment, name='appointment'),
    path('agendamento/sucesso/', views.appointment_success, name='appointment_success'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
]
