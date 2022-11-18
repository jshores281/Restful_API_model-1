
# Configures schema for request responses


from models.vault1_model import Vault1_Model
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field



class Vault1_Schema(SQLAlchemyAutoSchema):
	id = auto_field()
	name = auto_field()
	email = auto_field()
	website = auto_field()
	password = auto_field()
	created_on = auto_field() 
	updated_on = auto_field()
	class Meta:
		model = Vault1_Model
		include_relationships = True
		load_instance = True 




