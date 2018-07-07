from models.item import ItemModel
from services.helper import to_dict

class ItemService():
    
    @classmethod
    def get_all_items(cls):
        '''Returns the all location values as dictonary format'''
        item_values = ItemModel.get_all_items()
        item_list = to_dict(item_values)
        return item_list

    
    @classmethod
    def find_by_category(cls,category):
        item_values = ItemModel.find_by_category(category)
        item_list = to_dict(item_values)
        
        if item_values is not None:
            return item_list
        
        return None

    @classmethod
    def insert_item(cls,item):
        item = ItemModel(item.item_category, item.type_of_item)
        item.insert_item()
