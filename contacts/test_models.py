from django.test import TestCase
from .models import Contact

# Create your tests here.
class TestModels(TestCase):
    
    def test_new_contact_is_not_important_by_default(self):
        contact = Contact(name='Jane', email='jane@example.com', phone='123456789')
        contact.save()
        self.assertFalse(contact.important)
        
    def test_can_create_important_contact(self):
        contact = Contact(name='Jane', email='jane@example.com', phone='123456789', important=True)
        contact.save()
        self.assertTrue(contact.important)
    