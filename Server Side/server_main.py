
import random
import string

import argparse
import testcl_packager

import time
import os
import json

from flask import Flask
from flask_restful import Resource, Api, reqparse

job_queue = []

def random_string(n):
    return ''.join(random.SystemRandom().choice('0123456789') for _ in range(n))

class FileList(Resource):
    def get(self):
        #with open('tests.json') as tests:
            #json_tests = json.load(tests)
        #print("SENT",json.dumps(self.package, indent=4))
        result = self.package
        result['token'] = random_string(16)
        return result

class TimeRemaining (Resource):
    def get(self):
        return str((time.time() - self.start_time)//60)+' minutes have elapsed'

class StartQueue (Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_solutions', type=dict, help='List of solutions')
        args = parser.parse_args()
        job = {
                'done': False,
                'info': args
                }
        job_id = len(job_queue)
        job_queue.append(job)
        return str(job_id), 202

class GetResult (Resource):
    def get(self, job_id):
        job = job_queue[job_id]
        if 'done' in job and job['done'] == True:
            return job, 200
        else:
            return job, 302


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
    TimeRemaining.start_time = time.time()

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(FileList,      '/')
    api.add_resource(TimeRemaining, '/time')
    api.add_resource(StartQueue,    '/compile')
    api.add_resource(GetResult,     '/queue/<int:job_id>')

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


    with open(config_file) as config_opened:
        config = json.loads(config_opened.read())
        print("CONFIG", config)
        user_solns = {"quicksort_hs": "qsort=id", "recursion": "        gobbledy gook\n"}
        score = evaluate_user_solution(user_solns, config)
        print("SCORE:", score)
