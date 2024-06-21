import requests
import json
def get_warehouses(api_key):
    url = 'https://api.novaposhta.ua/v2.0/json/'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "apiKey": api_key,
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {}
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json().get('data', [])
    return []