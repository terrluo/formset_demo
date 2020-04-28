from datetime import datetime
from typing import Dict
from typing import Union

from django.test import TestCase
from django.urls import reverse

from demo.models import Book


class DemoViewTestCase(TestCase):
    pass
    # def setUp(self) -> None:
    #     self.data = {
    #         'form-TOTAL_FORMS': 2,
    #         'form-INITIAL_FORMS': 0,
    #         'form-MIN_NUM_FORMS': 1,
    #         'form-MAX_NUM_FORMS': 1000,
    #     }  # type: Dict[str, Union[int, str, datetime.date]]
    #
    # def test_index_get(self):
    #     resp = self.client.get(reverse('demo:index'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertContains(resp, 'Book')
    #
    # def test_index_post_invalid(self):
    #     resp = self.client.post(reverse('demo:index'), data=self.data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertContains(resp, '这个字段是必填项。')
    #
    # def test_index_post_valid(self):
    #     name = 'Book Name'
    #     author = 'Author'
    #     pub_date = datetime.now().date()
    #     self.data.update({
    #         'form-0-name': name,
    #         'form-0-author': author,
    #         'form-0-pub_date': pub_date,
    #     })
    #     resp = self.client.post(reverse('demo:index'), data=self.data)
    #     self.assertEqual(resp.status_code, 200)
    #     book = Book.objects.first()
    #     self.assertEqual(book.name, name)
    #     self.assertEqual(book.author, author)
    #     self.assertEqual(book.pub_date, pub_date)
    #     self.assertEqual(Book.objects.count(), 1)
