import logging
from flask_restplus import Api

log = logging.getLogger(__name__)
description = 'API for <App>'

api = Api(version='2.2.3', title='App API', description=description,
          ordered=False, doc='/doc')