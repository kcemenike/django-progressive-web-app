from django.test import TestCase
from django.urls import reverse
from ..models import Feed

# Create your tests here.


class Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Feed.objects.create(
            author='test author', title='test title', body='test body', slug='test-slug')

    def test_index_page_success(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertContains(response, 'Feeds')

    def test_getdata(self):
        response = self.client.get(reverse('getdata'))
        self.assertEqual(response.status_code, 200)

    def test_getjson(self):
        response = self.client.get(reverse('getjson'))
        self.assertEqual(response.status_code, 200)
        result = response.json()
        expected = "[{'id': 1, 'author': 'test author', 'title': 'test title', 'body': 'test body', 'slug': 'test-slug'}]"
        # self.assertJSONEqual(result, expected)
        # print(response.json())
