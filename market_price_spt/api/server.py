from flask import Flask, url_for
from flask_restful import Api

from market_price_spt.api.api import PriceSptCoreApi
from market_price_spt.api.info import PriceSptCoreInfo


def startAPIServer():
    app = Flask(__name__)
    api = Api(app)
    ##
    ## Actually setup the Api resource routing here
    ##
    api.add_resource(PriceSptCoreInfo, "/")
    api.add_resource(PriceSptCoreApi, "/<string:base_currency>/<string:quote_currency>")
    with app.test_request_context():
        print(url_for("pricesptcoreinfo"))
        print(url_for("pricesptcoreapi", base_currency="foo", quote_currency="bar"))
    return app
