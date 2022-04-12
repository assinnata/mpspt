from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("task")


class PriceSptCoreApi(Resource):
    def __init__(self):
        pass

    def get(self, base_currency, quote_currency):
        return {"price": 0}

    def put(self, base_currency, quote_currency):
        return {"success": True}, 201
