from models.location import LocationModel
from services.helper import to_dict

class LocationService():

    @classmethod
    def get_all_locations(cls):
        '''Returns the all location values as dictonary format'''
        location_values = LocationModel.get_all_loaction()
        location_list = to_dict(location_values)
        return location_list