from file_preprocessor import FileView
from subprocess import Popen
import tempfile
import os
import json


def franken_interpreter(file_view, user_solutions, file_pointer):
    in_question = False
    for line_data in file_view.line_datas:
        if 'macro' in line_data:
            if line_data['text'][0:18] == '@@ begin question ' and \
                    line_data['text'][18:-1] in user_solutions:
                in_question = True
                file_pointer.write(
                    user_solutions[line_data['text'][18:-1]])
            if line_data['text'][0:15] == '@@ end question':
                in_question = False
        elif not in_question:
            file_pointer.write(line_data['text'])


def run_user_solution(user_solutions, command, exam_config, stdin_input):
    base_dir = os.getcwd()
    with tempfile.TemporaryDirectory() as compiler_folder:
        for file_name in exam_config['file_list']:
            if os.path.dirname(file_name) != str():
                os.makedirs(compiler_folder + "\\" +
                            os.path.dirname(file_name), exist_ok=True)
            with open(compiler_folder + "\\" + file_name, mode="w") \
                    as compiler_input:

                with open(file_name) as code_file:
                    franken_interpreter(FileView(code_file),
                                        user_solutions, compiler_input)
        os.chdir(compiler_folder)
        stdin = stdin_input
        print("A")
        (stdout, stderr) = Popen(command, shell=True).communicate(stdin)
        print("B")
        os.chdir(base_dir)
        return (stdout, stderr)


def evaluate_user_solution(user_solutions, exam_config):
    score = 0
    for test_file in exam_config['test_list']:
        with open(test_file) as test_config:
            test_cases = json.loads(test_config.read())
            for test_case in test_cases:
                expected = run_user_solution(
                    {}, test_case['run'], exam_config, test_case['input'])
                user_inputs = {}
                for key, value in user_solutions.items():
                    if key in test_case['questions']:
                        user_inputs[key] = value
                actual = run_user_solution(user_inputs, test_case[
                                           'run'], exam_config,
                                           test_case['input'])
                if actual[0] == expected[0]:
                    score += test_case['points']
                else:
                    print("Expected:\n", expected[0],
                          "\n\nActual:\n", actual[0])
    return score
