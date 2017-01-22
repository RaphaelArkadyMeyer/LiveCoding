from random import randint


def generate_scores(question_file, test_case_file):
    x = randint(8, 15)
    real_scores = list(map(lambda x: randint(0, 100), range(x)))
    return list(map(lambda x:
                    {'real_test_score': real_scores[x],
                     'max_test_score': 100,
                     'name': "Question {}".format(x),
                     'real_question_score': 20 if real_scores[x] == 100 else 0,
                     'max_question_score': 20},
                    range(x)))


def get_user_solutions_file(file_name):
    user_solns = {}
    in_question = False
    soln_body = ''
    question_name = ''
    with open(file_name) as script:
        for line_number, line in enumerate(script):
            if line[0:18] == '@@ begin question ':
                question_name = line[18:-1]
                in_question = True
            elif line[0:15] == '@@ end question':
                in_question = False
                user_solns[question_name] = soln_body
            elif line[0:2] != '@@':
                if in_question:
                    soln_body += line
    return user_solns


def get_all_user_solutions(file_list):
    user_solns = {}
    for file_name in file_list:
        user_solns.update(get_user_solutions_file(file_name))
    return user_solns
