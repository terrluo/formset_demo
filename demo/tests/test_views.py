import logging

from django.test import TestCase
from django.urls import reverse

from demo.models import Company, Employee


class DemoViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(name='公司1')
        print('{}创建成功'.format(cls.company))
        cls.employee = Employee.objects.create(name='员工1', company=cls.company)
        print('{}创建成功'.format(cls.employee))

    def setUp(self) -> None:
        self.data = {
            'employees-TOTAL_FORMS': '1',
            'employees-INITIAL_FORMS': '0',
            'employees-MIN_NUM_FORMS': '1',
            'employees-MAX_NUM_FORMS': '1000',
        }


class CompanyCreateViewTestCase(DemoViewTestCase):
    @classmethod
    def setUpTestData(cls):
        super(CompanyCreateViewTestCase, cls).setUpTestData()
        cls.url = reverse('demo:company_create')

    def test_get(self):
        resp = self.client.get(self.url)
        self.assertContains(resp, '表单集实例')

    def test_post_invalid(self):
        resp = self.client.post(self.url, self.data)
        self.assertContains(resp, '这个字段是必填项。')

    def test_post_valid(self):
        self.data.update({
            'name': '公司2',
            'employees-0-name': '员工2',
            'employees-0-company': '',
            'employees-0-id': '',
        })
        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Company.objects.filter(name='公司2').exists())
        self.assertTrue(Employee.objects.filter(name='员工2').exists())


class CompanyUpdateViewTestCase(DemoViewTestCase):
    @classmethod
    def setUpTestData(cls):
        super(CompanyUpdateViewTestCase, cls).setUpTestData()
        cls.url = reverse('demo:company_update', kwargs={'company_id': cls.company.id})

    def test_get(self):
        resp = self.client.get(self.url)
        self.assertContains(resp, '公司1')

    def test_post_invalid(self):
        resp = self.client.post(self.url, self.data)
        self.assertContains(resp, '这个字段是必填项。')

    def test_post_valid(self):
        self.data.update({
            'name': '公司1',
            'employees-0-name': '员工2',
            'employees-0-company': '',
            'employees-0-id': self.employee.id,
        })
        self.assertTrue(Employee.objects.filter(name='员工1').exists())
        self.assertFalse(Employee.objects.filter(name='员工2').exists())

        resp = self.client.post(self.url, self.data)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Employee.objects.filter(name='员工2').exists())
