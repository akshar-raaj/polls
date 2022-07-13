import time
from threading import Thread

import datetime
import random
import logging

from polls.models import Question


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class QuestionFactory(object):

    @staticmethod
    def _get_proper_noun():
        nouns = [
            'bill', 'steve', 'mark', 'satya', 'sheryl', 'ratan',
            'anand', 'shiv', 'larry', 'sergey'
        ]
        index = random.randint(0, len(nouns) - 1)
        return nouns[index]

    @staticmethod
    def _get_adjective():
        choices = [
            'fantastic', 'awesome', 'fair', 'effective', 'motivating',
            'inspirational'
        ]
        index = random.randint(0, len(choices) - 1)
        return choices[index]

    @staticmethod
    def _get_collective_noun():
        choices = [
            'manager', 'leader', 'executive', 'president',
            'director', 'engineer'
        ]
        index = random.randint(0, len(choices) - 1)
        return choices[index]

    @staticmethod
    def create():
        proper_noun = QuestionFactory._get_proper_noun()
        adjective = QuestionFactory._get_adjective()
        collective_noun = QuestionFactory._get_collective_noun()
        now = datetime.datetime.now()
        question_text = 'Is {} a {} {}'.format(proper_noun, adjective, collective_noun)
        question = Question.objects.create(question_text=question_text, pub_date=now)
        return question


class Writer(Thread):

    def __init__(self, num_times):
        self.num_times = num_times
        super(Writer, self).__init__()

    def run(self):
        start = datetime.datetime.now()
        logger.info("Start: {}".format(start,))
        for i in range(self.num_times):
            QuestionFactory.create()
        end = datetime.datetime.now()
        logger.info("End: {}".format(end,))


def write_questions(num_threads, num_times):
    """
    This mimics num_thread concurrent connections.

    Thus when one connection is being processed, other connection would be waiting in queue.

    Also, a connection would make num_times requests. Thus we can notice some continuous requests and see how the load increases.
    :return:
    """

    threads = []
    start = time.time()
    for _ in range(num_threads):
        t = Writer(num_times)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()
    logger.info("Took {} seconds".format(end-start))


if __name__ == '__main__':
    write_questions()