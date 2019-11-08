from flask import Flask
from flask_restful import Resource, Api

app = Flask(_name_)
api = Api(app)


class HelloWord(Resource):
def get(self):
return {'hello': 'world'}


api.add_resource(HelloWord, '/')

if _name_ == '_name_':
app.run(debug=True, host='0.0.0.0')