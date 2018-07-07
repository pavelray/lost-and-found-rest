from utility.database import db


class LocationModel(db.Model):
    '''Location Table'''
    __tablename__ = 'LOCATION_TBL'
    country = db.Column('country', db.String(200))
    state = db.Column('state', db.String(200))
    city = db.Column('city', db.String(50))
    id = db.Column('location_id', db.BigInteger, primary_key=True)
   
    def __init__(self,country,state,city):
        self.state = state
        self.country = country
        self.city =city

    def as_dict(self):
        '''Return the object as dictonary format'''
        return dict(id=self.id, city=self.city,state=self.state,country=self.country)

    @classmethod
    def get_all_loaction(cls):
        '''Retruns all location values'''
        value = cls.query.all()
        return value
       