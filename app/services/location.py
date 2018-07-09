import json
import os.path

from models.location import LocationModel
from services.helper import to_dict

my_path = os.path.abspath(os.path.dirname(__file__))
city_path = os.path.join(my_path, "../data/cities.json")
country_path = os.path.join(my_path, "../data/countries.json")

class LocationService():

    @classmethod
    def get_all_locations(cls):
        '''Returns the all location values as dictonary format'''
        location_values = LocationModel.get_all_loaction()
        location_list = to_dict(location_values)
        return location_list

    @classmethod
    def get_all_cities(cls):
        '''Returns all cities'''
        cities = json.load(open(city_path,encoding="utf8"))
        
        return cities

    @classmethod
    def get_all_countries(cls):
        '''Returns all countries'''
        countries = json.load(open(country_path,encoding="utf8"))
        
        return countries
    
    @classmethod
    def get_cities_by_countries(cls,country_code):
        '''Returns all cities based on country'''
        cities = json.load(open(city_path,encoding="utf8"))
        match = list(d for d in cities if d['country'] == country_code)
                
        return match