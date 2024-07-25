from django.urls import path
from .views import FileUploadView, CheckCartaoView2

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('check/', CheckCartaoView2.as_view(), name='check_final'),
]
