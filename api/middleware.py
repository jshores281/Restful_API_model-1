

import sqlalchemy.orm.scoping as scoping
from sqlalchemy.exc import SQLAlchemyError


class SQLAlchemySessionManager:
    def __init__(self, Session):
        self.Session = Session

    def process_request(self, req, resp, resource):
        resource.session = self.Session()
  
    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            Session.remove()


