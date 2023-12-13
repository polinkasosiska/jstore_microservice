#integration testing
#для корзины
import unittest
from app import app, cart

class TestCartService(unittest.TestCase):
   def setUp(self):
       self.app = app.test_client()

   def test_get_cart(self):
       response = self.app.get('/cart')
       self.assertEqual(response.status_code, 200)
       self.assertEqual(len(response.json), len(cart))

   def test_add_to_cart(self):
       new_item = {"id": 4, "name": "New Jewelry", "price": 300}
       response = self.app.post('/cart', json=new_item)
       self.assertEqual(response.status_code, 201)
       self.assertEqual(response.json, {"message": "Item added to cart"})

   # Добавьте здесь другие тесты

if __name__ == '__main__':
   unittest.main()
