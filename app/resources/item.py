from flask_restful import Resource, reqparse, request


from services.item import ItemService
from models.item import ItemModel
from services.helper import to_dict

class Item(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        '''Get all the Items'''
        try:
            value = ItemService.get_all_items()
            return value , 200
        except Exception as e:
            return {'message': str(e)}, 500

    def post(self):
        data = request.get_json(silent=True)
        if ItemService.find_by_category(data['item_category']) is not None:
            return {'message': "An item with category '{}' already exists.".format(data['item_category'])}, 400

        item = ItemModel(data['item_category'],data['type_of_item'])

        try:
            ItemService.insert_item(item)
        except Exception as e:
            return {"message": str(e)}, 500

        return {"message": "Success"}, 201
