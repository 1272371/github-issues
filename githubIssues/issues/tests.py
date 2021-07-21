from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home
from .views import issues


class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_issues_url_resolves_issues_view(self):
        view = resolve('/issues')
        self.assertEquals(view.func, issues)
    
    def test_issues_request(self):
        
