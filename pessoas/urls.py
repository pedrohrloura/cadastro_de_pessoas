from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.list_person),
    url(r'^cadastro/',views.generate_name)
]