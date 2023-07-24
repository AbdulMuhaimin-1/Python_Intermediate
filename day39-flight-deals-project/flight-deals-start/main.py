from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from pprint import pprint


# flight_data = FlightData()
data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_data_destination()   # stores the data under the prices key in a variable

DESTINATION_CITY = "LON"

if sheet_data[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for each_row in sheet_data:
        each_row['iataCode'] = flight_search.get_destination_code(each_row['city'])
    print(f"Sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days= (6 * 30))

for destination in sheet_data:
    flight_search = FlightSearch()
    flight = flight_search.flight_check(
        DESTINATION_CITY,
        destination['iataCode'],
        travel_date_from=tomorrow,
        travel_date_to=six_month_from_today
    )

    if flight.price < destination['lowestPrice']:
        notification_manager.send_notification(
            message_to_send=f"Low price alert! Only £{flight.price} to fly from\n{flight.city_from}-{flight.airport_from} to "
                    f"{flight.destination_city}-{flight.destination_airpot}, from\n{flight.out_date} to {flight.return_date}"
        )


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
