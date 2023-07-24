class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, city_from, airpot_from, destination_city, destination_airpot, out_date, return_date):
        self.price = price
        self.city_from = city_from
        self.airport_from = airpot_from
        self.destination_city = destination_city
        self.destination_airpot = destination_airpot
        self.out_date = out_date
        self.return_date = return_date
