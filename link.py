BASE_URL = "https://google.com/"

def get():
    return {"base URL": BASE_URL}

def replace(text):
    response = {
        "response_type" : "in_channel",
        "text" : BASE_URL + (text.decode("utf-8"))
        # TODO: figure out why this is coming in empty!
    }
    return response
