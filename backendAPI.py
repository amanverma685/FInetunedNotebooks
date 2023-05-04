from flask import Flask, request
import json
from cosineSimilarity import getAPIResponse 

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def my_api():
    # get the JSON payload from the request
    data = request.json

    # process the data and return a response
    result = process_data(data)
    return result

def process_data(data):
    # do some processing on the data
    print(data)
    
    result = getAPIResponse(data['data'])

    # return the result
    return result

if __name__ == '__main__':
    app.run()