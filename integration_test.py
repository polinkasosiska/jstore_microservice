import pytest
from flask import Flask
from list_products import app
import asyncio

@pytest.fixture
def client():
   app.config['TESTING'] = True
   with app.test_client() as client:
       yield client

@pytest.mark.asyncio
async def test_get_jewelry(client):
   response = await client.get('/jewelry')
   assert response.status_code == 200
   assert len(response.json) == 3 # Проверяем, что в ответе 3 элемента

@pytest.mark.asyncio
async def test_get_jewelry_by_id(client):
   response = await client.get('/jewelry/1')
   assert response.status_code == 200
   assert response.json['id'] == 1 # Проверяем, что id равен 1

@pytest.mark.asyncio
async def test_add_jewelry(client):
   response = await client.post('/jewelry', json={"id": 4, "name": "New Jewelry", "price": 300})
   assert response.status_code == 201
   assert response.json['id'] == 4 # Проверяем, что id нового элемента равен 4

@pytest.mark.asyncio
async def test_update_jewelry(client):
   response = await client.put('/jewelry/1', json={"name": "Updated Jewelry", "price": 400})
   assert response.status_code == 200
   assert response.json['name'] == "Updated Jewelry" # Проверяем, что имя обновлено

@pytest.mark.asyncio
async def test_delete_jewelry(client):
   response = await client.delete('/jewelry/1')
   assert response.status_code == 200
   assert response.json['message'] == "Item deleted" # Проверяем, что сообщение об удалении пришло
