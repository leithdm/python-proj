import requests
from pprint import pprint
GET_SHEETY_ENDPOINT = "https://api.sheety.co/d15280c76a0f04fa51809228e94ef4ce/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_all_data(self):
        response = requests.get(GET_SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        endpoint = "https://api.sheety.co/d15280c76a0f04fa51809228e94ef4ce/flightDeals/prices"

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{endpoint}/{city['id']}",
                json=new_data
            )

            print(response.text)
