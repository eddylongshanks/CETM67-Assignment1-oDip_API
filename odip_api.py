""" Script for oDip API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from requests import post
import json

SNS_API = "https://fm6o6wnr3l.execute-api.eu-west-2.amazonaws.com/dev/send"
API_KEY = "G5MWtixDKN3xgHcJkWqfc6tTa1a3ZBIv5TE2dVKZ"
API_HEADERS = {"x-api-key":API_KEY}

app = Flask(__name__)
api = Api(app)

class SendEnquiry(Resource):
    def post(self):
        try:            
            data = request.json
            json_data = json.loads(json.dumps(data))

            response = post(SNS_API, headers=API_HEADERS, json=json_data)

            log(response.text)

            return {
                'statusCode': response.status_code,
                'body': json.dumps(str(response.text))
            }

        except Exception as e:
            log(e)
            return {
                'statusCode': 500,
                'body': json.dumps(str(e))
            }
            raise


class GetLog(Resource):
    def get(self):
        f = open('odip_log.txt', 'r')
        return f.read()


class HealthCheck(Resource):
    def get(self):
        return {
            'statusCode': 200,
            'body': 'oDip API Available'
        }

## Routing ##
api.add_resource(SendEnquiry, '/send-enquiry')
api.add_resource(GetLog, '/log')
api.add_resource(HealthCheck, '/')

# Methods

def log(data_to_save):
    # Logs data to a local file for debugging
    with open('odip_log.txt', 'w') as log_file:
        log_file.write(str(data_to_save))

if __name__ == "__main__":
    app.run(debug=True, port=5001)