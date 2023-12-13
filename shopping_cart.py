from flask import Flask, jsonify, request

# Создаем Flask приложение
app = Flask(__name__)

# Список элементов в корзине
cart = []

# Эндпоинт для получения списка украшений в корзине
@app.route("/cart", methods=['GET'])
def get_cart():
  return jsonify(cart)

# Эндпоинт для добавления украшения в корзину
@app.route("/cart", methods=['POST'])
def add_to_cart():
  item = request.get_json()
  cart.append(item)
  return jsonify({"message": "Item added to cart"}), 201

# Эндпоинт для очистки корзины/\
@app.route("/cart", methods=['DELETE'])
def clear_cart():
  cart.clear()
  return jsonify({"message": "Cart cleared"}), 200

# Эндпоинт для удаления украшения из корзины
@app.route("/cart/<int:id>", methods=['DELETE'])
def remove_from_cart(id):
  for item in cart:
      if item["id"] == id:
          cart.remove(item)
          return jsonify({"message": "Item removed from cart"}), 200
  return jsonify({"error": "Item not found in cart"}), 404

# Запуск Flask приложения
if __name__ == "__main__":
  app.run(port=8001)
