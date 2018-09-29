from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import json

# Create your tests here.
class TestAdd(TestCase):
	
	def setup(self):
		self.client = Client()

	def test_add(self):
		c = self.client.post(reverse('add'), data={'name':"yyyy", "address":"jjjjj"})
		c = json.loads(c.content)
		self.assertEqual(c["status"],"success")
		
	def test_home(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertTemplateUsed(response, 'home.html')
