from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pets
from form import AddPetForm, EditPetForm

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_ECHO']= True
app.config['SECRET_KEY']= 'Fooster2023'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """Home route.  displays two forms, one adopted and one available for adoption"""
    #availpets = db.session.query(Pets).order_by(Pets.available.desc()).all()
    availpets = Pets.query.filter(Pets.available==True)
    adoptedPets  =Pets.query.filter(Pets.available==False)
   
    return render_template('home.html', pets=availpets, adoptedPets = adoptedPets)

@app.route('/<int:petid>', methods=["GET", "POST"])
def editPet(petid):
   """Edits  a pet"""
   update_pet=Pets.query.get(petid)
   """This is needed becuase the form works with strings and they are in bool form from database"""
   if update_pet.available == True:
      update_pet.available = 'true'
   else:
      update_pet.available= 'false'

   form = EditPetForm(obj=update_pet)

   if form.validate_on_submit():
      updatedPet = Pets.query.get(petid)
      name= form.name.data
      
      species = form.species.data
      photo_url = form.photo_url.data
      age = form.age.data
      notes = form.notes.data
      if form.available.data == 'false':
       available = False
      else:
       available = True
      
      updatedPet.update(name, species, photo_url, age, notes, available)
   
      db.session.add(updatedPet)
      db.session.commit()
      return redirect('/')
   
   
   
   return render_template('edit_pet.html', form=form)
   

@app.route('/add' , methods=["GET", "POST"])
def addPet():
    """Form for adding a pet"""
    form = AddPetForm()

    if form.validate_on_submit(): 
     name= form.name.data
     species = form.species.data
     photo_url = form.photo_url.data
     age = form.age.data
     notes = form.notes.data
     newPet = Pets(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
     db.session.add(newPet)
     db.session.commit()
     return redirect('/')
    return render_template('add_pet.html', form=form)
    
