from models.lostandfound import LostAndFoundModel
from services.helper import to_dict


class LostAndFoundService():
    
    @classmethod
    def get_all_lost_found_items(cls):
        '''Returns the all lost and found items in dictonary format'''
        lost_found_items = LostAndFoundModel.get_all_lost_found_items()
        if lost_found_items is None:
            return None    
        
        lost_found_list = to_dict(lost_found_items) 
        return lost_found_list

    @classmethod
    def get_lost_found_items_by_description(cls,search_key):
        '''Returns the matched items by search key in item description'''
        lost_found_items = LostAndFoundModel.get_lost_found_items_by_description(search_key)
        if lost_found_items is None:
            return None 
        
        lost_found_list = to_dict(lost_found_items) 
        return lost_found_list

    @classmethod
    def get_all_lost_items(cls):
        '''Returns all lost items'''
        lost_items = LostAndFoundModel.get_all_lost_items()
        if lost_items is None:
            return None
        
        lost_items_list = to_dict(lost_items)
        return lost_items_list

    @classmethod
    def get_all_found_items(cls):
        '''Returns all lost items'''
        found_items = LostAndFoundModel.get_all_found_items()
        if found_items is None:
            return None
        
        found_items_list = to_dict(found_items)
        return found_items_list

    @classmethod
    def save_lost_found_item(cls,item_number,location_id,picture,last_seen_at,is_found,email_id,first_name,last_name,contact_number,description):
        '''Save Lost and Found Item in Database'''
        lost_found_obj = LostAndFoundModel(item_number,location_id,picture,last_seen_at,is_found,email_id,first_name,last_name,contact_number,description)
        lost_found_obj.save_lost_found_item()
