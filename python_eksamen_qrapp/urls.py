from django.urls import path

from . import views

app_name = 'python_eksamen_qrapp'

urlpatterns = [
    path('', views.index, name='index'),
]

