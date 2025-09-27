import unittest
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

class TestApp(unittest.TestCase):
    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert "status" in response.json()
      
