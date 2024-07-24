from django.urls import path
from .views import Home, FileUploadView

urlpatterns = [
    # path('hello/', hello_world, name='hello-world'),
    path('', Home.as_view()),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]