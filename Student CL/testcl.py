
# coding: utf-8
import click
import random
import communication
import requests
import os
import json
import time as thyme # because reasons

from evaluator import generate_scores

try:
    range_type = xrange
except NameError:
    range_type = range


@click.group()
def cli():
    ("This script communicates with the Instructors' server"
     " to prepare your exam.")
    pass


@cli.command()
def progress():
    """Demonstrates the progress bar."""

    items = range_type(20)

    def process_slowly(item):
        thyme.sleep(0.002 * random.random())

    def filter(items):
        for item in items:
            if random.random() > 0.3:
                yield item

    with click.progressbar(filter(items), label='Compiling Offline',
                           fill_char=click.style('#', fg='green')) as bar:
        for item in bar:
            process_slowly(item)

    score_info = generate_scores('in', 'tests')
    name_length = max(map(lambda x: len(x['name']), score_info))
    real_score = 0
    max_score = 0
    for index, question_info in enumerate(score_info):
        real_score += question_info['real_test_score']
        real_score += question_info['real_question_score']
        max_score += question_info['max_test_score']
        max_score += question_info['max_question_score']
        with click.progressbar(length=question_info['max_test_score'],
                               label=question_info['name'].ljust(
                                   name_length, ' '),
                               show_pos=True,
                               bar_template='%(label)s  %(bar)s | %(info)s',
                               fill_char=click.style(u'█', fg='cyan'),
                               empty_char=' ') as bar:
            bar.update(question_info['real_test_score'])

    with click.progressbar(length=max_score,
                           show_pos=True,
                           label='Total Progress for File',
                           fill_char=click.style(u'█', fg='green')) as bar:
        bar.update(real_score)


@cli.command()
def time():
    """Returns the amount of time remaining in the session."""
    click.echo(communication.get_time())


@cli.command()
def clear():
    """Clears the entire screen."""
    click.clear()


@cli.command()
def checkout():
    ip_addr    = 'localhost:5000'#click.prompt("Enter IP address and port")
    login_user = ''#click.prompt("Enter User Login")
    login_pass = ''#click.prompt("Enter User Pass", hide_input=True)

    response = communication.get_exam_info('localhost:5000', login_user, login_pass)

    tests = response['tests']
    files = response['files']
    token = response['token']

    click.echo(tests)

    put_in_directory(files)
    with open('testcases.json', mode='w') as json_file:
        json_file.write(json.dumps(tests, indent=4, sort_keys=True))

    communication.set_session(ip_addr, login_user, token)


def put_in_directory(file_list, directory=os.getcwd()):
    for name, value in file_list.items():
        new_path = os.path.join(directory, name)
        if isinstance(value, dict):
            os.mkdirs(new_path, exist_ok=True)
            put_in_directory(value, new_path)
        elif isinstance(value, str):
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            with open(new_path, mode='w') as new_file:
                new_file.write(value)


@cli.command()
@click.pass_context
def turnin(ctx):
    ctx.forward(progress)


@cli.command()
def testCases():
  """TestCases for each question."""
  menu = 'testcases'
  while 1:
     if menu == 'testcases':
        click.secho(' Testcases: ', fg='green')        
        # open json file and put data in dictionary
        # change path of json after the student server for questions and testcases is craeted 
        with open(r'\Users\Lena Adel\Documents\LiveCoding\examples\input1.json') as data_file:
                test_casses = json.load(data_file)
        # traverse json add list of questions
        quest_test_dict = {} 
        for test_case in test_casses:
             for question in test_case['questions']:
                if question in quest_test_dict: 
                    quest_test_dict[question].append(test_case)
                else: 
                    quest_test_dict[question] = [test_case]
        # print out list of question options
        # list of question optuons
        quest_dict = {}
        for index, question in enumerate(quest_test_dict):
             click.secho("     " + str(index + 1) + '. ' + question, fg='green')
             quest_dict[index+1] = question
        option_q =int(input(" Enter question number: "))
        click.echo("\n")
        click.clear()
        click.secho("<<<<<<<<<<<<<<<<< " + quest_dict.get(option_q) + " >>>>>>>>>>>>>>>>>>>\n",fg='green', bold=True)
        # print out the test casses
        for index, test_case in enumerate(quest_test_dict.get(quest_dict.get(option_q))): 
              click.secho("<<<<<<<<<<<<<<<<< " + "TestCase " + str(index + 1) + " >>>>>>>>>>>>>>>>>>>>\n", fg='green', bold=True)
              click.secho("                Total points: " + str(test_case['points']), bold=True)
              click.secho(" Input: ", bold=True)    
              click.echo(" " + test_case['input'] + "\n")
        
        menu = 'exit'
     elif menu == 'exit':
        return     
