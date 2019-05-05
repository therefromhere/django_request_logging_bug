from django.test import TestCase

# Create your tests here.

class MyTest(TestCase):

    def test_bug(self):
        self.client.post("/bug/create/")