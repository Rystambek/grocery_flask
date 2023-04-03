import requests
import json

fruit = {
            "name": "Barry",
            "quantity": 2,
            "price": 2.4,
            "type": "fruit"
        }
r = requests.post('http://127.0.0.1:5000/grocery/add',json=fruit)
print(r.json())