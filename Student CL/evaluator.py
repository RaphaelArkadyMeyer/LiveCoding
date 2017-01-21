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
