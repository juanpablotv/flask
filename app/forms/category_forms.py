from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required

class CreateCategory(FlaskForm):
    category = StringField('Categoria',
                           validators=[data_required])
