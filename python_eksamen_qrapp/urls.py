from django.urls import path

from . import views

app_name = 'python_eksamen_qrapp'

urlpatterns = [
    path('', views.index, name='index'),
    #path('new_qr_web/', views.new_qr_web,name='new_qr_web')
]

