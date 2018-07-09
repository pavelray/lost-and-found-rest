from flask_restful import Resource, reqparse

from services.location import LocationService


class Location(Resource):
    def get(self):
        '''Get Method'''
        '''Return all locations'''
        try:
            value = LocationService.get_all_locations()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

class City(Resource):
    def get(self):
        '''Get Method'''
        '''Return all Cities'''
        try:
            value = LocationService.get_all_cities()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

class CityByCountry(Resource):
    def get(self,country_code):
        '''Get Method'''
        '''Return all Cities by Country'''
        try:
            value = LocationService.get_cities_by_countries(country_code)
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

class Country(Resource):
    def get(self):
        '''Get Method'''
        '''Return all Countries'''
        try:
            value = LocationService.get_all_countries()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500
