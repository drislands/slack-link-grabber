from flask import abort
import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['VERIFICATION_TOKEN']
base_url = os.environ['BASE_URL']

def get():
    return {"base URL": base_url}

def replace(text,token):
    if token == verification_token:
        response = {
            "response_type" : "in_channel",
            "text" : base_url + text
        }
    else:
        abort(
            401, "Unverified request."
        )
    return response
