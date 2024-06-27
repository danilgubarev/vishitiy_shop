from django.conf import settings
import requests


class NovaPoshta:
    def __init__(self):
        self.api_url = "https://api.novaposhta.ua/v2.0/json/"
        self.api_key = settings.NOVAPOSHTA_KEY

    def send(self, model_name: str, method: str, **params):
        resp = requests.post(
            self.api_url,
            json={
                "apiKey": self.api_key,
                "modelName": model_name,
                "calledMethod": method,
                "methodProperties": params
            },
            headers={"Content-Type": "application/json"},
        )
        print('got response')
        return resp.json()

    def get_cities(self, **params):
        print("Getting cities")
        return self.send("Address", "getCities", **params)

    def get_post_offices(self, **params):
        print("Getting post offices")
        return self.send("AddressGeneral", "getWarehouses", **params)
