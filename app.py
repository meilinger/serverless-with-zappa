import editdistance
from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


class EditDistance(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('str1', required=True)
    parser.add_argument('str2', required=True)

    def get(self):
        args = self.parser.parse_args()
        distance = editdistance.eval(args.get('str1'), args.get('str2'))
        return {'distance': distance}


api.add_resource(EditDistance, '/edit-distance/')

if __name__ == '__main__':
    app.run(debug=True)
