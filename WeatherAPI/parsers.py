from flask_restful import reqparse
from WeatherAPI import validators
    
# Define the following Parsers
# NOTE: Use the custom 'datestring' validator defined in 'WeatherAPI/validators.py' for validating input date string.
# 1. WeatherRequestParser : It parses the values of input fields-  'id', 'date', 'temperature', and 'location', present in a JSON entry
## The value of 'location' field is another json entry, whose values are parsed by LocationParser

class WeatherRequestParser():
    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", )
        parser.add_argument("date", )
        parser.add_argument("temperature", )
        parser.add_argument("location", )

        args = parser.parse_args()
        return args


# 2. LocationParser : It parses the values of input fields - 'lat', 'lon', 'city', and 'state', passed to 'location' field of weather JSON input entry.
class LocationParser():
    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("lat", )
        parser.add_argument("lon", )
        parser.add_argument("city", )
        parser.add_argument("state", )

        args = parser.parse_args()
        return args


# 3. WeatherGetParser : It parses the values of input fields - 'date', 'lat' and 'lon', present in a query string.
class WeatherGetParser():
    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "date", help="The date is required.", required=True
        )
        parser.add_argument(
            "lat", help="The lat is required.", required=True
        )
        parser.add_argument(
            "log", help="The lon is required.", required=True
        )
        args = parser.parse_args()
        return args


# 4. WeatherEraseParser : It parses the values of input fields - 'start', 'end', 'lat' and 'lon', present in  a query string
class WeatherEraseParser():
    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("start", )
        parser.add_argument("end", )
        parser.add_argument("lat", )
        parser.add_argument("lon", )

        args = parser.parse_args()
        return args


# 5. TemperatureGetParser : It parses the values of input fields - 'start', 'end', present in  a query string
class TemperatureGetParser():
    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("start", )
        parser.add_argument("end", )

        args = parser.parse_args()
        return args


# 6. PreferredLocationsParser : It parses the values of input fields - 'date', 'lat' and 'lon', present in  a query string
class PreferredLocationsParser():
    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("date", )
        parser.add_argument("lat", )
        parser.add_argument("lon", )

        args = parser.parse_args()
        return args
