# API resource endpoints allow interaction through server to DB.

import sys
import falcon
import json

from models import vault1_model
from schemas.vault1_schema import *

import engine
from engine.db_con import *



# THIS ACTUALY WORKS (TIP: START SMALL THEN WORK ALL THE WAY UP)
class Vault1_resource:
	def on_get(self, req, resp):

		# retreives list of all objects from DB.Vault1
		obj = session.query(Vault1_Model).all()

		# serializes data from DB into json response
		resp.media = Vault1_Schema(many=True).dump(obj)

		# request code responses
		resp.status = falcon.HTTP_200
		resp.content_type = falcon.MEDIA_JSON

	def on_post(self, req, resp):

		# serializer
		obj = req.get_media()
		schema_ = Vault1_Schema()

		# formats into json
		dump_data = schema_.dump(obj)
		load_data = schema_.load(dump_data, session=session)

		# loads json serialized object into DB
		session.add(load_data)
		session.commit()

		# deserializer
		resp.text = json.dumps(obj)

		# request code responses
		resp.status = falcon.HTTP_200
		resp.content_type = falcon.MEDIA_JSON



	def on_put(self, req, resp, _id):
		# INCOMPLETE, ISSUES WITH QUERYING AND RETREIVING DATA, ID OBJECT MATCHING

		obj = session.query(Vault1_Model).filter(Vault1_Model.id==_id)
		new_data = json.load(req.bounded_stream)
        
		for data in obj:
			data.update(new_data)

		# deserializer
		resp.text = json.dumps(obj)

		# request code responses
		resp.status = falcon.HTTP_200
		resp.content_type = falcon.MEDIA_JSON		



	def on_delete(self, req, resp):
		pass













