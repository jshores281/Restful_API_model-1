# Main API application.

import os
import sys
import json
from datetime import datetime
from functools import partial

import falcon_sqla
import falcon
from falcon import media

from falcon_apispec import FalconPlugin
from falcon_apispec import *
from apispec import APISpec

from resources.vault1_resource import *
from models import *
from engine import *



class DatetimeEncoder(json.JSONEncoder):
    """Json Encoder that supports datetime objects."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


json_handler = media.JSONHandler(
    dumps=partial(json.dumps, cls=DatetimeEncoder),
)
extra_handlers = {
    'application/json': json_handler,
}


manager = falcon_sqla.Manager(Session)
api = falcon.API(
	media_type='application/json',
	middleware=[manager.middleware])


# GENERATE A REST API SWAGGER PAGE
# spec = APISpec(
#     title='Falcon vault Swagger page',
#     version='2.0.0',
#     openapi_version='3.0.0',
#     plugins=[FalconPlugin(api)],
#     )


api.req_options.media_handlers.update(extra_handlers)
api.resp_options.media_handlers.update(extra_handlers)


vault1_resource = Vault1_resource()
api.add_route('/vault1', vault1_resource)
api.add_route('/vault1/{_id}', vault1_resource)

# api.add_route('/docs/swagger.json', FalconPlugin(spec))
# api.add_route('/docs/', FalconPlugin(spec))


