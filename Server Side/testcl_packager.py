import json
from file_preprocessor import get_student_view_json


def make_testcl_package(config_file):
    config = None
    with open(config_file) as file:
        config = json.loads(file.read())

    testcl_package = {}

    testcl_file_list = {}
    for file_name in config['file_list']:
        testcl_file_list[file_name] = get_student_view_json(file_name)
    testcl_package['files'] = testcl_file_list

    testcl_test_list = []
    for file_name in config['test_list']:
        with open(file_name) as test_file:
            testcl_test_list += json.loads(test_file.read())
    testcl_package['tests'] = testcl_test_list

    return(json.dumps(testcl_package))
