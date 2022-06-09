import pytest
import datetime

from django.utils import timezone

from .models import Question


class TestModels():

    @pytest.mark.django_db
    def test_question_published_recently(self):
        pub_date = timezone.now()
        question = Question.objects.create(question_text="How's the weather?",
                                           pub_date=pub_date)
        assert question.was_published_recently() is True

    @pytest.mark.django_db
    def test_question_not_published_recently(self):
        pub_date = timezone.now() - datetime.timedelta(days=2)
        question = Question.objects.create(question_text="How's the weather?",
                                           pub_date=pub_date)
        assert question.was_published_recently() is False