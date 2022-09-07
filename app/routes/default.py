import json
import flask
from flask_restplus import Resource
from mongoengine import Q
from flask import current_app as app

from app.api import api
from app.errors.common import JsonParseError
from app.models.DefaultModel import DefaultModel

default_ns = api.namespace(
    'Default',
    description='Default namespace',
    path='/default'
)


@default_ns.route('')
class Default(Resource):
    """Base default resource"""

    def get(self):
        app.logger.info("This is a logger!")
        query_id = flask.request.args['id']

        # query = Q()
        # query &= Q(id=query_id)

        res = DefaultModel.objects.get(id=query_id)

        return {
            'results': res.as_dict() if res else None
        }

    def post(self):
        try:
            data = json.loads(flask.request.data)
        except ValueError as error:
            raise JsonParseError() from error

        model = DefaultModel()
        model.text = data.get('text', None)
        model.save()

        return {
            'model': model.as_dict()
        }

    def put(self):
        pass

    def delete(self):
        pass
