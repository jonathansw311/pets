from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL



class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name Required!")])
    species = SelectField("Species", choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')], validators=[InputRequired(message="Species Required!")])
    photo_url = StringField("Photo Url", validators=[URL(require_tld=True, message="Must be url")])
    age = IntegerField("Pet Age", validators=[InputRequired(message="Pet Age Required!"), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name Required!")])
    species = SelectField("Species", choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')], validators=[InputRequired(message="Species Required!")])        
    photo_url = StringField("Photo Url")
    age = IntegerField("Pet Age", validators=[InputRequired(message="Pet Age Required!"), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes")
    available = SelectField("Avalability", choices=[('true','Available'), ('false', 'Adopted!')])