from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from .views import home_page
from .models import Item

class HomePageTest(TestCase):
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     expcted_html = render_to_string('lists/home.html', request=request)
    #     self.assertEqual(response.content.decode(), expcted_html)
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

        