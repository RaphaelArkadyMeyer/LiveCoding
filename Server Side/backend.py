
import os
import json

from flask import Flask
from flask_restful import Resource, Api

def directory_listing_json(path=os.getcwd()):
    dirs = os.listdir(path)
    result = {}
    for d in dirs:
        if os.path.isdir(d):
            pass
            #result[d] = directory_listing_json(os.path.join(path,d))
        elif os.path.isfile(d):
            with open(d) as open_d:
                result[d] = json.dumps(open_d.read())
    return result

class FileList(Resource):
    def get(self):
        #with open('tests.json') as tests:
            #json_tests = json.load(tests)
        return {
                'files': directory_listing_json(),
                'tests': None#json.dumps(json_tests)
                }

def main():
    #with open('config.json') as config:
    #    test_config = json.load(config)

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(FileList, '/')

    app.run(debug=True)


if __name__ == '__main__':
    main()
