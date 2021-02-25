import json
file = '1.json'
def validate(filename):
    with open(filename) as file:
        try:
            return json.load(file) # put JSON-data to a variable
        except JSONDecodeError:
            print("Invalid JSON") # in case json is invalid
