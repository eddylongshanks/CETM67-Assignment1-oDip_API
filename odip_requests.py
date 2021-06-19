""" DB Requests
"""

import json
from requests import post, get

BASE_URL = "http://127.0.0.1:5000"
#BASE_URL = "http://ec2-18-130-251-69.eu-west-2.compute.amazonaws.com"

# GET all enquiries
# response = get(BASE_URL + "/get-all-enquiries")
# response_data = json.dumps(response.text)
# print(response.text)


# CREATE a new enquiry
data = {
    "id": "hnjknlsaa8327343",
    "first_name": "Bob",
    "last_name": "Smith",
    "building": "11",
    "street": "Indigo Avenue",
    "town": "Newcastle",
    "county": "Tyne and Wear",
    "postcode": "NE2 3JM",
    "telephone_number": "07777777778",
    "email_address": "test@holmescentral.co.uk",
    "preferred_time_to_contact": "S",
    "annual_income": "30000",
    "loan_amount": "10000",
    "property_value": "100000",
    "mortgage_type": "RM",
    "ltv_value": "5"
}

# response = post(BASE_URL + "/send_enquiry")

response = post(BASE_URL + "/send-enquiry", json = data)
print(response.text)
