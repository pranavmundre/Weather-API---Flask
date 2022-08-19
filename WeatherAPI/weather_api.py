import datetime as dt
import json
import math

from flask import Flask, request, Response, Blueprint

from WeatherAPI.models import db, Location, Weather

from flask_restful import Resource, Api, fields, marshal

from WeatherAPI.parsers import WeatherRequestParser, WeatherGetParser, LocationParser, WeatherEraseParser, TemperatureGetParser, PreferredLocationsParser
from WeatherAPI.marshallers import resource_fields, temp_fields, no_temp_fields, location_fields, preferred_location_details

weather_bp = Blueprint('WeatherAPI', __name__)

weatherapi = Api(weather_bp)


class WeatherList(Resource):

    def get(self):
        pass
        

    def post(self):
        pass


class WeatherErase(Resource):

    def delete(self):
        pass

    
class LocationTemp(Resource):

    def get(self):
        pass
       

class WeatherAPI(Resource):
    
    def get(self):
        pass

    def post(self):
        args = WeatherRequestParser.get_arguments(self)

        weather_data = Weather()
        
        db.add(weather_data)   
        db.commit()
        return Response({}, 400)


class WeatherEraseAPI(Resource):
    
    def get(self):
        pass

    def delete(self):
        try:
            num_rows_deleted = db.session.query(Weather).delete()
            db.session.commit()
        except:
            db.session.rollback()
        return Response({}, 200)


class TemperatureAPI(Resource):
    
    def get(self):
        pass


class PreferredLocationsAPI(Resource):
    
    def get(self):
        pass

weatherapi.add_resource(WeatherAPI, '/weather')
weatherapi.add_resource(WeatherEraseAPI, '/erase')
weatherapi.add_resource(TemperatureAPI, '/weather/temperature')
weatherapi.add_resource(PreferredLocationsAPI, '/weather/locations')

