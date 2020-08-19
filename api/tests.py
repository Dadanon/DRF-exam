from django.test import TestCase
import requests


class APITestCase(TestCase):

    def test_list_content_api(self):
        url = 'http://127.0.0.1:8000/api/v1/1/'
        response = requests.get(url)

        title = f"{response.json()['title']}"
        body = f"{response.json()['body']}"

        self.assertEqual(title, 'First posty')
        self.assertEqual(body, 'Super post about what? I dont know nihira')

