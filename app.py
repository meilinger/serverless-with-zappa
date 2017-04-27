import os
import pylev
from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app, catch_all_404s=True)


class EditDistance(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('str1', required=True)
    parser.add_argument('str2', required=True)

    def get(self):
        args = self.parser.parse_args()
        distance = pylev.levenschtein(args.get('str1'), args.get('str2'))
        print 'Distance from {} to {} is {}'.format(args.get('str1'), args.get('str2'), distance)
        print os.environ
        return {
            'distance': distance
        }


api.add_resource(EditDistance, '/edit-distance/')

if __name__ == '__main__':
    app.run(debug=True)
