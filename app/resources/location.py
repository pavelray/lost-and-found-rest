from flask_restful import Resource, reqparse


from services.location import LocationService

class Location(Resource):
    def get(self):
        '''Get all the locations'''
        try:
            value = LocationService.get_all_locations()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500
