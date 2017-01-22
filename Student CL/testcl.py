# coding: utf-8
import click
import time
import random
import communication
import os
import json

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
        time.sleep(0.002 * random.random())

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
def clear():
    """Clears the entire screen."""
    click.clear()


@cli.command()
def checkout():
    ip_addr    = 'localhost:5000'#click.prompt("Enter IP address and port")
    login_user = ''#click.prompt("Enter User Login")
    login_pass = ''#click.prompt("Enter User Pass", hide_input=True)

    response = communication.get_exam_info('localhost:5000', login_user, login_pass)
    print('response:',json.dumps(response,indent=4))

    tests = response['tests']
    files = response['files']

    click.echo(tests)
    print('files:',json.dumps(files,indent=4))

    put_in_directory(files)


def put_in_directory(file_list, directory=os.getcwd()):
    for name, value in file_list.items():
        new_path = os.path.join(directory, name)
        print('old path =', directory)
        print('file     =', name)
        print('new_path =', new_path)
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
