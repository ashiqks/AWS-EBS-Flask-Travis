from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse, Api
import json

application = Flask(__name__)

@application.route('/', methods=['POST'])
def hello():
    d = json.loads(request.data)
    d['datas'] = d['datas'] + 'Got it baby'
    print(d)
    #print('the data', d)
    #print(type(d))
    return jsonify(d)


if __name__ == '__main__':
    application.run(debug=True)

