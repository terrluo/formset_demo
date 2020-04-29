from datetime import date, timedelta
from typing import Any
from typing import Dict

from django.test import TestCase
from django.urls import reverse

from demo.models import Book


class DemoViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(name='name', pub_date=date.today())

    def setUp(self) -> None:
        self.data = {
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 1,
            'form-MIN_NUM_FORMS': 1,
            'form-MAX_NUM_FORMS': 1000,
        }  # type: Dict[str, Any]

    def test_index(self):
        resp = self.client.get(reverse('demo:index'))
        self.assertContains(resp, 'book')
        self.assertContains(resp, 'book_list')

    def test_book_get(self):
        resp = self.client.get(reverse('demo:book'))
        self.assertContains(resp, 'name')
        self.assertContains(resp, str(date.today()))

    def test_book_post_invalid(self):
        resp = self.client.post(reverse('demo:book'), data=self.data)
        self.assertContains(resp, '这个字段是必填项。', count=3)

    def test_book_post_delete_book(self):
        self.data.update({
            'form-0-id': self.book.id,
            'form-0-name': self.book.name,
            'form-0-pub_date': self.book.pub_date,
            'form-0-DELETE': 'on',
        })
        self.assertEqual(Book.objects.count(), 1)
        resp = self.client.post(reverse('demo:book'), data=self.data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Book.objects.count(), 0)

    def test_book_post_add_book(self):
        tomorrow = date.today() + timedelta(days=1)
        self.data.update({
            'form-0-id': self.book.id,
            'form-0-name': self.book.name,
            'form-0-pub_date': self.book.pub_date,
            'form-0-DELETE': '',
            'form-1-id': '',
            'form-1-name': 'name2',
            'form-1-pub_date': tomorrow,
            'form-1-DELETE': '',
        })
        self.assertEqual(Book.objects.count(), 1)
        resp = self.client.post(reverse('demo:book'), data=self.data)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Book.objects.filter(name='name2').exists())
        self.assertEqual(Book.objects.count(), 2)

    def test_book_list(self):
        resp = self.client.get(reverse('demo:book_list'))
        self.assertContains(resp, self.book.name)
