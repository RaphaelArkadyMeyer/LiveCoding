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
                'files': json.loads(self.package),
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

    print(testcl_packager.make_testcl_package(config_file))

    FileList.package = testcl_packager.make_testcl_package(config_file)

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(FileList, '/')

    app.run(debug=True)


if __name__ == '__main__':
    # main()

    from file_preprocessor import FileView
    from frankencompiler import franken_interpreter, run_user_solution, evaluate_user_solution
    import tempfile
    import subprocess

    args = argparse.ArgumentParser(
        description='Prepare a testcl package for students\' exams.')
    args.add_argument('config file', type=str,
                      help='The config file associated with the exam.')
    config_file = vars(args.parse_args())['config file']

    # print(testcl_packager.make_testcl_package(config_file))

    with open(config_file) as config_opened:
        config = json.loads(config_opened.read())
        print("CONFIG", config)
        user_solns = {"quicksort_hs": "qsort=id", "recursion": "        return arr\n"}
        evaluate_user_solution(user_solns, config)
        #run_user_solution(user_solns, "python examples/quicksort.py", config, "5\n3 2 5 1 4")
