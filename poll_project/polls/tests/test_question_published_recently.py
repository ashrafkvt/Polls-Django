import pytest
import datetime

from django.utils import timezone

from polls.models import Question

@pytest.mark.django_db
def test_was_published_recently_with_future_question():
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    future_question.save()
    assert future_question.was_published_recently() is False
