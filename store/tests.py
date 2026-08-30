from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status


class CategoryTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='teste',
            password='12345678'
        )

        self.client.force_authenticate(
            user=self.user
        )

    def test_criar_categoria(self):

        response = self.client.post(
            '/api/categories/',
            {
                'name': 'Eletronicos',
                'description': 'Produtos eletronicos'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_listar_categorias(self):

        response = self.client.get(
            '/api/categories/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )