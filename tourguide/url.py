from django.conf.urls import url,include
from . import views


app_name = 'user'

urlpatterns = [
    url(r'user/',views.UserCreate.as_view(),name='CreateUser'),
    url(r'index/',views.IndexView.as_view(),name='index'),

]