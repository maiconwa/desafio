from django.test import TestCase
from rest_framework.test import APIRequestFactory
from myapp.views import FileUploadView, CheckCard


class FileUploadViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FileUploadView.as_view()
        self.file_content = b"Your file content goes here"

    def test_file_upload(self):
        request = self.factory.post('/upload/', {'file': self.file_content}, format='multipart')
        response = self.view(request)
        self.assertEqual(response.status_code, 401)
        # Add more assertions as needed


class CheckCardTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CheckCard.as_view()
        self.card_data = [
            {'numero_cartao': 'your_card_number_1'},
            {'numero_cartao': 'your_card_number_2'},
            # Add more card data as needed
        ]

    def test_check_card(self):
        request = self.factory.post('/check-card/', self.card_data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 401)
        # Add more assertions as needed
