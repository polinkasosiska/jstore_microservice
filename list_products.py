from flask import Flask, jsonify

# Создаем Flask приложение
app = Flask(__name__)

# Список ювелирных украшений
jewelry_items = [
 {"id": 1, "name": "Ring", "price": 100},
 {"id": 2, "name": "Necklace", "price": 200},
 {"id": 3, "name": "Earrings", "price": 50},
]

# Эндпоинт для получения списка всех украшений
@app.route("/jewelry", methods=['GET'])
def get_jewelry():
 return jsonify(jewelry_items)

# Эндпоинт для получения информации о конкретном украшении по его идентификатору
@app.route("/jewelry/<int:id>", methods=['GET'])
def get_jewelry_by_id(id):
 for item in jewelry_items:
     if item["id"] == id:
         return jsonify(item)
 return jsonify({"error": "Item not found"}), 404

# Эндпоинт для добавления нового украшения
@app.route("/jewelry", methods=['POST'])
def add_jewelry():
 new_item = {"id": 4, "name": "New Jewelry", "price": 300}
 jewelry_items.append(new_item)
 return jsonify(new_item), 201

# Эндпоинт для обновления информации об украшении
@app.route("/jewelry/<int:id>", methods=['PUT'])
def update_jewelry(id):
 for item in jewelry_items:
     if item["id"] == id:
         item["name"] = "Updated Jewelry"
         item["price"] = 400
         return jsonify(item)
 return jsonify({"error": "Item not found"}), 404

# Эндпоинт для удаления украшения/\
@app.route("/jewelry/<int:id>", methods=['DELETE'])
def delete_jewelry(id):
 for item in jewelry_items:
     if item["id"] == id:
         jewelry_items.remove(item)
         return jsonify({"message": "Item deleted"}), 200
 return jsonify({"error": "Item not found"}), 404

# Эндпоинт для главной страницы
@app.route('/')
def home():
  return """
	<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />
  <title>Browser</title>
</head>

<body>
  <h1>
    Добро пожаловать в микросервис jstore
  </h1>
  <p>
    Приколочено гвоздями!
    <img src="https://www.vprommetiz.ru/wp-content/uploads/2020/05/gvozdi-stroitelnye01.jpg" alt="Гвозди!" />
  </p>
</body>

</html> 
"""

# Запуск Flask приложения
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=8080)
