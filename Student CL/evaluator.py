from random import randint


def generate_scores(question_file, test_case_file):
    x = randint(8, 15)
    return list(map(lambda x:
                    {'real_score': randint(0, 100),
                     'max_score': 100,
                     'name': "Question {}".format(x)},
                    range(x)))
