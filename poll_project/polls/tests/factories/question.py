import factory

from django.utils import timezone

from polls.models import Question

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
    
    question_text = factory.sequence(lambda n: f"how are you user-{n}?")
    pub_date = factory.LazyFunction(timezone.now)