from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from .models import Group, Student


User = get_user_model()


class TestUser(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser',
            email='test@user.com',
            password='totalsecurity'
        )
        test_user.save()

    def test_login_redirect(self):
        login_required_url = reverse('student_create')
        resp = self.client.get(login_required_url)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.url.startswith('/accounts/login/'))

    def test_user_login(self):
        resp = self.client.post(
            reverse('login'),
            {
                'query': 'testuser',
                'password': 'totalsecurity'
            }
        )
        self.assertEqual(resp.status_code, 302)

    def test_group_create_by_authenticated_user(self):
        group_create_url = reverse('group_create')
        student_create_url = reverse('student_create')
        student_id = '123765'

        login = self.client.login(username='testuser', password='totalsecurity')
        resp = self.client.post(group_create_url, {'name': 'test group'})
        self.assertEqual(resp.status_code, 302)

        group = Group.objects.get(id=1)

        resp = self.client.post(
            student_create_url,
            {
                'id': student_id,
                'first_name': 'first',
                'last_name': 'last',
                'middle_name': 'middle',
                'birth_d': '2000-01-01',
                'group_id': '1',
            }
        )
        self.assertEqual(resp.status_code, 302)

        student = Student.objects.get(id=student_id)
