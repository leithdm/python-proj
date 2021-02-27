import requests

endpoint = f"https://api.sheety.co/d15280c76a0f04fa51809228e94ef4ce/flightDeals/prices"

new_data = {
    "price": {
        "iataCode": "fuckyou"
    }
}
response = requests.put(
    url=f"{endpoint}/{2}",
    json=new_data
)

print(response.text)
