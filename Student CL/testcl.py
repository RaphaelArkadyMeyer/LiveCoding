# coding: utf-8
import click
import time
import random
import communication

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
    ip_addr    = click.prompt("Enter IP address and port")
    login_user = click.prompt("Enter User Login")
    file_list = communication.get_exam_info(login_user, ip_addr)
    click.echo("List of Files")
    for index, file_info in enumerate(file_list):
        click.echo("{} | {}".format(index + 1, file_info['file_name']))


@cli.command()
@click.pass_context
def turnin(ctx):
    ctx.forward(progress)
