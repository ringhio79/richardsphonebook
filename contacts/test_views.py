from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):
    
    def test_root_url(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contacts/contact_list.html")