# myapp/urls.py
from django.urls import path
from .views import user_info_form, success_page

urlpatterns = [
    path('', user_info_form, name='user_info_form'),
    path('user_info_form/', user_info_form, name='user_info_form'),
    path('success_page/', success_page, name='success_page'),
]
