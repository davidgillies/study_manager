from django.core.urlresolvers import resolve
from django.test import TestCase
from dashboard.views import index
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_dashboard_returns_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<!doctype html>'))
        self.assertIn(b'<title>Dashboard</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
