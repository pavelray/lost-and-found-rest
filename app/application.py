from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from utility.security import authenticate,identity
from utility.createapp import create_app
from resources.lostandfound import LostAndFound , Lost, Found, LostAndFoundByKey
from resources.location import Location, City , Country , CityByCountry
from resources.item import Item
  

application = create_app()
api = Api(application)
jwt = JWT(application,authenticate,identity)
    
    
api.add_resource(LostAndFound,'/lost_found/')
api.add_resource(Lost,'/lost/')
api.add_resource(Found,'/found/')
api.add_resource(LostAndFoundByKey,'/lost_found/<string:search_key>')
api.add_resource(Location,'/location/')
api.add_resource(City,'/cities/')
api.add_resource(CityByCountry,'/cities/<string:country_code>')
api.add_resource(Country,'/countries/')
api.add_resource(Item,'/items/')

if __name__ == '__main__':    
    application.run(debug=True)