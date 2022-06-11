"""
This contains all the views of the polls application
"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    """
    The index view of polls application.
    It shows the latest 5 questions.
    :param request:
    :return:
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    This shows the detail of a particular question.
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(_, question_id):
    """
    This shows results of a given question.
    :param request:
    :param question_id:
    :return:
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(_, question_id):
    """
    This allows voting on a particular question.
    :param request:
    :param question_id:
    :return:
    """
    message = "You're voting on question"
    return HttpResponse(f"{message} {question_id}.")
