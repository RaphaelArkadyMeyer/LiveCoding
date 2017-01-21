
import os.path as path

from sys import argv
from json import load
from os import system
from subprocess import Popen




def ask_client_for_file(file_name):
    return open(file_name)


def make_frankenstein(question_names, file_name):
    global server_directory
    global client_directory


def read_json(file_name):
    with open(file_name) as input_file:
        return load (input_file)

def run_tests(tests, config):
    file_dict = {}
    for f in config:
        file_name = f['file']
        for question_name in f['questions']:
            file_dict[question_name] = file_name
    for test in tests:
        questions  = test['questions']
        stdin      = test['input']
        args       = test['args']
        files_made = []
        # TODO possibly redundant
        for question in questions:
            file_name = file_dict[question]
            if file_name not in files_made:
                make_frankenstein(questions, file_name)
                files_made.append(file_name)
        #system(config['compile'])
        #(stdout, stderr) = Popen(args).communicate(stdin)



def main():
    config = read_json(argv[1])
    tests = read_json(argv[2])
    global server_directory
    global client_directory
    server_directory = read_json(argv[3])
    client_directory = read_json(argv[4])
    run_tests(tests, config)

if __name__ == '__main__':
    main()

