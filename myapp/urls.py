from django.urls import path
from .views import FileUploadView, CheckCard

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('check/', CheckCard.as_view(), name='check-card'),
]
