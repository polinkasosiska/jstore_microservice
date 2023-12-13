#unit testing Микросервис каталога
import unittest
from app import app, jewelry_items

class TestJewelryService(unittest.TestCase):
   def setUp(self):
       self.app = app.test_client()

   def test_get_jewelry(self):
       response = self.app.get('/jewelry')
       self.assertEqual(response.status_code, 200)
       self.assertEqual(len(response.json), len(jewelry_items))

   def test_get_jewelry_by_id(self):
       for item in jewelry_items:
           response = self.app.get(f'/jewelry/{item["id"]}')
           self.assertEqual(response.status_code, 200)
           self.assertEqual(response.json, item)

   # Добавьте здесь другие тесты

if __name__ == '__main__':
   unittest.main()
