import pytest
import datetime

from django.utils import timezone

from polls.models import Question
from polls.tests.factories.question import QuestionFactory

@pytest.mark.django_db
def test_was_published_recently_with_future_question():
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = QuestionFactory.create(pub_date=time)
    assert future_question.was_published_recently() is False

@pytest.mark.django_db
def test_was_published_recently_with_old_question():
    time = timezone.now() - datetime.timedelta(days=2, minutes=60)
    old_question = Question(pub_date=time)
    old_question.save()
    assert old_question.was_published_recently() is False

@pytest.mark.django_db
def test_was_published_recently_with_recent_question():
    recent_question = QuestionFactory.create()
    assert recent_question.was_published_recently() is True