from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from .views import home_page
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expcted_html = render_to_string('lists/home.html', request=request)
        print(expcted_html)
        self.assertEqual(response.content.decode(), expcted_html)
