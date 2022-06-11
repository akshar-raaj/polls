"""
This tracks all the models needed for the polls application.
"""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    This is used to track different questions of the polls application.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        Tells if a question was published in the last 24 hours.
        :return:
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    This is used to track choices for a question.
    One question can have multiple choices,
    thus it's a one-to-many relationship from question to choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
