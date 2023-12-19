import pytest
from flask import Flask
from list_products import app #Замените на имя вашего файла с приложением

@pytest.fixture
def client():
   app.config['TESTING'] = True
   with app.test_client() as client:
       yield client

def test_get_jewelry(client):
   response = client.get('/jewelry')
   assert response.status_code == 200
   assert len(response.json) == 3 #Проверяем, что в ответе 3 элемента

def test_get_jewelry_by_id(client):
   response = client.get('/jewelry/1')
   assert response.status_code == 200
   assert response.json['id'] == 1 #Проверяем, что id равен 1

def test_add_jewelry(client):
   response = client.post('/jewelry', json={"id": 4, "name": "New Jewelry", "price": 300})
   assert response.status_code == 201
   assert response.json['id'] == 4 #Проверяем, что id нового элемента равен 4

def test_update_jewelry(client):
   response = client.put('/jewelry/1', json={"name": "Updated Jewelry", "price": 400})
   assert response.status_code == 200
   assert response.json['name'] == "Updated Jewelry" #Проверяем, что имя обновлено

def test_delete_jewelry(client):
   response = client.delete('/jewelry/1')
   assert response.status_code == 200
   assert response.json['message'] == "Item deleted" #Проверяем, что сообщение об удалении пришло

