from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^send_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.send_login_email, name='login'),
    url(r'^logout$', views.send_login_email, name='logout'),
]