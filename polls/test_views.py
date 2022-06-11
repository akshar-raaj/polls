import pytest
import datetime

from django.utils import timezone

from .models import Question


class TestViews():

    @pytest.mark.django_db
    @pytest.mark.polls_list
    def test_index(self, client):
        response = client.get('/polls/')
        assert response.status_code == 200

    @pytest.mark.django_db
    @pytest.mark.polls_list
    def test_index_num_questions(self, client):
        """
        This test asserts that latest n questions are shown by the index view.
        :return:
        """
        question_texts = [b'first', b'second', b'third', b'fourth', b'fifth', b'sixth']
        for question_text in question_texts:
            pub_date = timezone.now()
            question = Question.objects.create(question_text=question_text,
                                               pub_date=pub_date)

        response = client.get('/polls/')
        assert b'first' not in response.content
        for question_text in question_texts[1:]:
            assert question_text in response.content

    @pytest.mark.django_db
    @pytest.mark.parametrize('url_fragment', ['', 'results/', 'vote/'])
    @pytest.mark.polls_detail
    def test_detail_views(self, client, url_fragment):
        pub_date = timezone.now()
        question = Question.objects.create(question_text='How you doin? <Joey style>',
                                           pub_date=pub_date)
        response = client.get('/polls/{}/{}'.format(question.pk, url_fragment,))
        assert response.status_code == 200
