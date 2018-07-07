from utility.database import db

class ItemModel(db.Model):
    '''Item Table'''
    __tablename__ = 'ITEM_TBL'
    type_of_item = db.Column('type_of_item', db.String(200))
    item_category = db.Column('item_category', db.String(200))
    item_number = db.Column('item_number', db.BigInteger, primary_key=True)
   
    def __init__(self,item_type,item_category):
        self.type_of_item = item_type
        self.item_category = item_category

    def as_dict(self):
        '''Return the object as dictonary format'''
        return dict(item_number=self.item_number, item_category=self.item_category,type_of_item=self.type_of_item)

    @classmethod
    def get_all_items(cls):
        '''Retruns all items'''
        value = cls.query.all()
        return value

    @classmethod
    def find_by_category(cls,category):
        return cls.query.filter_by(item_category=category)

    def insert_item(self):
        db.session.add(self)
        db.session.commit()