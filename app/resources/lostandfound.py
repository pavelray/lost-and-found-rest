from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required

from services.lostandfound import LostAndFoundService
from models.lostandfound import LostAndFoundModel

class LostAndFound(Resource):
    
    def get(self):
        try:
            value = LostAndFoundService.get_all_lost_found_items()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

    def post(self):
        data = request.get_json(silent=True)
        lost_found_item = LostAndFoundModel(data['item_number'],data['location_id'],
                                data['picture'],data['last_seen_at'],data['is_found'], data['email_id']
                                ,data['first_name'],data['last_name'],data['contact_number'],data['description'])

        try:
            LostAndFoundService.save_lost_found_item(lost_found_item)
        except Exception as e:
            return {"message": str(e)}, 500

        return {"message": "Success"}, 201


class Lost(Resource):
    
    def get(self):
        try:
            value = LostAndFoundService.get_all_lost_items()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

    def put(self):
        pass

    def delete(self):
        pass


class Found(Resource):
    
    def get(self):
        try:
            value = LostAndFoundService.get_all_found_items()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

    def put(self):
        pass

    def delete(self):
        pass


class LostAndFoundByKey(Resource):
    
    def get(self,search_key):
        try:
            value = LostAndFoundService.get_lost_found_items_by_description(search_key)
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500
