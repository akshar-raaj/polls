import pytest
import datetime

from django.test import Client
from django.utils import timezone

from .models import Question


def test_polls():
    client = Client()
    response = client.get('/polls/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_model_question():
    pub_date = timezone.now()
    question = Question.objects.create(question_text="How's the weather?",
                                       pub_date=pub_date)
    assert question.was_published_recently() is True

    pub_date = timezone.now() - datetime.timedelta(days=2)
    question = Question.objects.create(question_text="How's the weather?",
                                       pub_date=pub_date)
    assert question.was_published_recently() is False
