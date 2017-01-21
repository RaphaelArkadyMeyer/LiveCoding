import argparse
import json
from random import randint

parser = argparse.ArgumentParser(
    description='Prepare a testcl package for students\' exams.')
parser.add_argument('config file', type=str,
                    help='The config file associated with the exam.')

config_file = vars(parser.parse_args())['config file']
config = None
with open(config_file) as file:
    config = json.loads(file.read())


def generate_file_list(config):
    file_list = list()
    for file_name in config['file_list']:
        file_list.append({'file_name': file_name,
                          'questions': randint(0, 5)})
    return file_list
