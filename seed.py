from models import Pets, db
from app import app

db.drop_all()
db.create_all()

pet = Pets(name='fluffy', species='cat', photo_url='http://adsfas', age=5, notes='no notes yet')

db.session.add(pet)
db.session.commit()