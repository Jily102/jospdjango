from django.urls import path
from .views import home, inboxPage, messagePage

urlpatterns = [
    path('', home, name='home'),
    path('inbox/', inboxPage, name='inbox'),
    path('message/<int:pk>', messagePage, name='message')
]