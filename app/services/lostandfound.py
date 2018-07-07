from models.lostandfound import LostAndFoundModel
from services.helper import to_dict


class LostAndFoundService():
    
    @classmethod
    def get_all_lost_found_items(cls):
        '''Returns the all lost and found items as dictonary format'''
        lost_found_items = LostAndFoundModel.get_all_lost_found_items()
        if lost_found_items is None:
            return None    
        
        lost_found_list = to_dict(lost_found_items) 
        return lost_found_list

    @classmethod
    def get_lost_found_items_by_description(cls,search_key):
        '''Returns the matched items by search key'''
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
    def save_lost_found_item(self,lost_found_obj):
        if lost_found_obj is not None:
            lost_found_obj = LostAndFoundModel(lost_found_obj.item_number,lost_found_obj.location_id,
                                lost_found_obj.picture,lost_found_obj.last_seen_at,lost_found_obj.is_found, lost_found_obj.email_id
                                ,lost_found_obj.first_name,lost_found_obj.last_name,lost_found_obj.contact_number,lost_found_obj.description)
            lost_found_obj.save_lost_found_item()
