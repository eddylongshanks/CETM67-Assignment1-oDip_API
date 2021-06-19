""" Script for oDip API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from requests import post
import json

SNS_API = "https://fm6o6wnr3l.execute-api.eu-west-2.amazonaws.com/dev/send"

app = Flask(__name__)
api = Api(app)

class SendEnquiry(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            post(SNS_API, body=data)

            return 'Enquiry Sent'
        except Exception as e:
            f = open('db_log.txt', 'w')
            f.write(str(e))
            f.close()
            raise


class GetLog(Resource):
    def get(self):
        f = open('db_log.txt', 'r')
        return f.read()

## Routing ##
api.add_resource(GetLog, '/log')
api.add_resource(SendEnquiry, '/send-enquiry')

if __name__ == "__main__":
    app.run(debug=True)