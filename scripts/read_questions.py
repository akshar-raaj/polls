import time
from threading import Thread

import datetime
import random
import logging

from polls.models import Question
from scripts.write_questions import QuestionFactory


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class ReaderFactory(object):

    @staticmethod
    def read():
        proper_noun = QuestionFactory._get_proper_noun()
        adjective = QuestionFactory._get_adjective()
        collective_noun = QuestionFactory._get_collective_noun()
        question_text = 'Is {} a {} {}'.format(proper_noun, adjective, collective_noun)
        questions = Question.objects.filter(question_text__contains=question_text)
        num_questions = len(questions)
        return num_questions


class Reader(Thread):

    def __init__(self, num_times):
        self.num_times = num_times
        super(Reader, self).__init__()

    def run(self):
        start = datetime.datetime.now()
        logger.info("Start: {}".format(start,))
        for i in range(self.num_times):
            ReaderFactory.read()
        end = datetime.datetime.now()
        logger.info("End: {}".format(end,))