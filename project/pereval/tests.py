from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pereval, MyUser, Coord, Level, Images

class PerevalAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = MyUser.objects.create(
            email="test@example.com",
            fam="Testov",
            name="Test",
            otc="Testovich",
            phone="+79999999999"
        )

        # Create test coord
        self.coord = Coord.objects.create(
            latitude="45.3842",
            longitude="7.1525",
            height="1200"
        )

        # Create test level
        self.level = Level.objects.create(
            winter="1A",
            summer="1B",
            autumn="1A",
            spring="1A"
        )

        # Create test pereval
        self.pereval = Pereval.objects.create(
            user=self.user,
            coord=self.coord,
            level=self.level,
            beauty_title="пер. ",
            title="Test Pass",
            other_title="Test",
            content="Test content",
            status="new"
        )

        # Create test image
        self.image = Images.objects.create(
            pereval=self.pereval,
            data="https://example.com/test.jpg",
            title="Test Image"
        )

    def test_create_pereval(self):
        url = '/pereval/submitData/'
        data = {
            "beauty_title": "пер. ",
            "title": "New Test Pass",
            "other_title": "New Test",
            "content": "New content",
            "user": {
                "email": "new@example.com",
                "fam": "New",
                "name": "User",
                "otc": "Testovich",
                "phone": "+78888888888"
            },
            "coord": {
                "latitude": "46.3842",
                "longitude": "8.1525",
                "height": "1300"
            },
            "level": {
                "winter": "1B",
                "summer": "2A",
                "autumn": "1B",
                "spring": "1A"
            },
            "images": [
                {
                    "data": "https://example.com/new.jpg",
                    "title": "New Image"
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.data)

    def test_get_pereval(self):
        url = f'/pereval/{self.pereval.id}/submitData/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Pass")

    def test_update_pereval(self):
        url = f'/pereval/{self.pereval.id}/submitData/'
        data = {
            "title": "Updated Test Pass",
            "other_title": "Updated Test",
            "content": "Updated content"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['state'], 1)

    def test_filter_by_email(self):
        url = '/pereval/submitData/?user__email=test@example.com'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Pass")

    def test_update_forbidden_fields(self):
        url = f'/pereval/{self.pereval.id}/submitData/'
        data = {
            "user": {
                "email": "changed@example.com",
                "phone": "+77777777777"
            }
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['state'], 0)