from utility.database import db


class LostAndFoundModel(db.Model):
    '''Lost and Found Table'''
    __tablename__ = 'LOST_FOUND_GLOBAL'
    lost_found_id = db.Column('LOST_FOUND_ID', db.BigInteger, primary_key=True)
    item_number = db.Column('ITEM_NUMBER', db.BigInteger)
    location_id = db.Column('LOCATION_ID', db.BigInteger)
    picture = db.Column('PICTURE', db.String(4000))
    last_seen_at = db.Column('LAST_SEEN_AT', db.String(200))
    is_found = db.Column('IS_FOUND', db.Integer)
    email_id = db.Column('EMAIL_ID', db.String(50))
    first_name = db.Column('FIRST_NAME', db.String(50))
    last_name = db.Column('LAST_NAME', db.String(50))
    contact_number = db.Column('CONTACT_NUMBER', db.BigInteger)
    description = db.Column('DESCRIPTION', db.String(4000))
    
    def __init__(self,item_number,location_id,picture,last_seen_at,is_found,email_id,first_name,last_name,contact_number,description):
        self.item_number=item_number
        self.location_id=location_id
        self.picture=picture
        self.last_seen_at=last_seen_at
        self.is_found=is_found
        self.email_id=email_id
        self.first_name=first_name
        self.last_name=last_name
        self.contact_number=contact_number
        self.description=description
   
    def as_dict(self):
        '''Return the object as dictonary format'''
        return dict(lost_found_id=self.lost_found_id,
                    item_number=self.item_number, 
                    location_id=self.location_id,
                    picture=self.picture,
                    last_seen_at=self.last_seen_at.isoformat(),
                    is_found=self.is_found,
                    email_id=self.email_id,
                    first_name=self.first_name,
                    last_name=self.last_name,
                    contact_number=self.contact_number,
                    description=self.description
                    )

    @classmethod
    def get_all_lost_found_items(cls):
        '''Retruns all loast and found items'''
        value = cls.query.all()
        return value

    @classmethod
    def get_lost_found_items_by_description(cls,search_key):
        '''Retruns all lost and found based on matching search key'''
        value = cls.query.filter(LostAndFoundModel.description.contains(search_key))
        return value

    @classmethod
    def get_all_lost_items(cls):
        '''Return all lost items'''
        value = cls.query.filter(LostAndFoundModel.is_found==0).all()
        return value

    @classmethod
    def get_all_found_items(cls):
        '''Return all lost items'''
        value = cls.query.filter(LostAndFoundModel.is_found==1).all()
        return value
    
    def save_lost_found_item(self):
        '''Save Lost and found Item on Database'''
        db.session.add(self)
        db.session.commit()
