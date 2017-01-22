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
        print("SENT",json.dumps(self.package, indent=4))
        return json.loads(self.package)

def main():
    #with open('config.json') as config:
    #    test_config = json.load(config)


    args = argparse.ArgumentParser(
        description='Prepare a testcl package for students\' exams.')
    args.add_argument('config file', type=str,
                      help='The config file associated with the exam.')
    config_file = vars(args.parse_args())['config file']

    print(testcl_packager.make_testcl_package(config_file))

    FileList.package = testcl_packager.make_testcl_package(config_file)

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(FileList, '/')

    app.run(debug=True)

if __name__ == '__main__':
    # main()


    import argparse
    import testcl_packager
    import file_preprocessor

    # args = argparse.ArgumentParser(
    #     description='Prepare a testcl package for students\' exams.')
    # args.add_argument('config file', type=str,
    #                   help='The config file associated with the exam.')
    # config_file = vars(args.parse_args())['config file']

    # print(testcl_packager.make_testcl_package(config_file))

    # user_solns = {"quicksort_hs": "qsort=id"}
    user_solns = {"recursion": "blueberries"}

    with open("examples/quicksort.py") as code_file:
        file_preprocessor.FileView(code_file).frankencompile(user_solns)

