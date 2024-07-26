from django.test import TestCase
from myapp.models import FileApi, CheckCartao


class FileApiTestCase(TestCase):
    def setUp(self):
        # Create a sample FileApi instance for testing
        self.file_api = FileApi.objects.create(
            nome="Test File",
            data="2024-07-25",
            lote="A123",
            quantidade_registro="100",
            numeracao_no_lote="456",
            numero_cartao="1234567890123456",
            unique="unique123"
        )

    def test_file_api_creation(self):
        # Check if the FileApi instance was created successfully
        self.assertEqual(self.file_api.nome, "Test File")
        self.assertEqual(self.file_api.data, "2024-07-25")
        # Add more assertions for other fields as needed

    # Add more test methods for other functionalities related to FileApi


class CheckCartaoTestCase(TestCase):
    def setUp(self):
        # Create a sample CheckCartao instance for testing
        self.check_cartao = CheckCartao.objects.create(
            numero_cartao="1234567890123456"
        )

    def test_check_cartao_creation(self):
        # Check if the CheckCartao instance was created successfully
        self.assertEqual(self.check_cartao.numero_cartao, "1234567890123456")

    # Add more test methods for other functionalities related to CheckCartao
