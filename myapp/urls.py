from django.urls import path
from .views import hello_world, Home

urlpatterns = [
    path('hello/', hello_world, name='hello-world'),
    path('', Home.as_view()),
]