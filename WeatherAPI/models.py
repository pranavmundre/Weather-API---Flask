import re
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Define two models : Location and Weather

# Location Model must contain the following attributes.
#    'id' - a primary key holding Integer value
#    'lat' - Float field
#    'lon' - Float field
#    'city' - String field of maximum length 100 characters.
#    'state' - String field of maximum length 100 characters.


# Weather Model must contain the following attributes.
#    'id' - a primary key holding Integer value
#    'date' - Date Time Field
#    '_temperature' - A string field to store 24 temperature values, separated by semicolon (';').
# Define a property named 'temparature', whose getter method returns 24 temperature values in a list and 
# setter method sets the joined temperature string to '_temperature'

# Establish one to many relationship between Location and Weather models.
# A location object must able to access associated weather details of the location using 'weathers' attribute, and
# A weather object must able to access associated location details using 'location' attribute.

class Location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lat = db.Column(db.Float, )
    lon = db.Column(db.Float, )
    city = db.Column(db.String, )
    state = db.Column(db.String,)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime,)
    _temperature = db.Column(db.String,)
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    # @temperature.getter
    # def temperature(self):
    #     return [i for i in self._temperature.split(";")]

    # @temperature.setter
    # def temperature(self):
        # self._temperature = ";".join(self._temperature)
