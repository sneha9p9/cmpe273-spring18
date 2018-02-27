from flask import Flask
from flask import request, jsonify
from flask import Response
import json

app = Flask(__name__)

result = {}
@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    #numb{} = '1'
    
    result['id'] = 1
    result['name'] = request.form["name"]
    #return json.dumps(result, indent=4, sort_keys=True)
    return Response(json.dumps(result, indent=4, sort_keys=True), status=201)
    #return "Hello {}!".format(result)

@app.route('/users/<id>', methods=['GET'])
def get_example(id):
    if (result['id'] == int(id)):
        return Response(json.dumps(result, indent=4, sort_keys=True), status=200)


@app.route('/users/<id>', methods=['DELETE'])
def del_example(id):
    if (result['id'] == int(id)):
        #del result['id'==int(id)]        
        #print (result.'id'.==int(id)])
        del result["id"]
        del result["name"]
        return Response("", status=204)
