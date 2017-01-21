import argparse
import testcl_packager

import os
import json

from flask import Flask
from flask_restful import Resource, Api

class FileList(Resource):
    def get(self):
        #with open('tests.json') as tests:
            #json_tests = json.load(tests)
        return {
                'files': self.package,
                'tests': None#json.dumps(json_tests)
                }

def main():
    #with open('config.json') as config:
    #    test_config = json.load(config)


    args = argparse.ArgumentParser(
        description='Prepare a testcl package for students\' exams.')
    args.add_argument('config file', type=str,
                      help='The config file associated with the exam.')
    config_file = vars(args.parse_args())['config file']

    FileList.package = testcl_packager.make_testcl_package(config_file)

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(FileList, '/')

    app.run(debug=True)

if __name__ == '__main__':
    main()
