import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "5G37rLfdajCoyVioJzx4gOBDZp2GahSG"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        hearders = {
            'apikey': TEQUILA_API_KEY
        }
        query = {
            "term" : city_name,
            "location_types" : "city"
        }

        response = requests.get(url=location_endpoint, headers=hearders, params=query)
        response.raise_for_status()
        result = response.json()['locations']
        code = result[0]['code']
        return  code

    def flight_check(self, travel_from_code, travel_to_code, travel_date_from, travel_date_to):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        parameters = {
            "fly_from": f"{travel_from_code}",
            "fly_to": f"{travel_to_code}",
            "date_from": f"{travel_date_from.strftime('%d/%m/%Y')}",
            "date_to": f"{travel_date_to.strftime('%d/%m/%Y')}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city" : 1,
            "max_stopovers" : 0,
            "curr": "GBP"
        }
        response = requests.get(url=search_endpoint, headers=headers, params=parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {travel_from_code}")
            return None

        flight_data = FlightData(
            price=data['price'],
            city_from=data['route'][0]['cityFrom'],
            airpot_from=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airpot=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][0]['local_departure'].split('T')[0]
        )
        # print(f"{flight_data.destination_city}: £{flight_data.price}")
        # print(f"From: {flight_data.city_from}-{flight_data.airport_from} to {flight_data.destination_city}-{flight_data.destination_airpot}")
        # print(f"{flight_data.out_date} to {flight_data.return_date}")
        return  flight_data