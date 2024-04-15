from django.core.management.base import BaseCommand
from main.models import QuizQuestion, QuizChoice

class Command(BaseCommand):
    help = 'Populate quiz questions and choices'

    def handle(self, *args, **kwargs):
        # Create quiz questions
        question1 = QuizQuestion.objects.create(question_text="What is the capital of France?")
        question2 = QuizQuestion.objects.create(question_text="What is the largest planet in our solar system?")

        # Create choices for question 1
        QuizChoice.objects.create(question=question1, choice_text="Paris", is_correct=True)
        QuizChoice.objects.create(question=question1, choice_text="London", is_correct=False)
        QuizChoice.objects.create(question=question1, choice_text="Berlin", is_correct=False)

        # Create choices for question 2
        QuizChoice.objects.create(question=question2, choice_text="Mars", is_correct=False)
        QuizChoice.objects.create(question=question2, choice_text="Jupiter", is_correct=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated quiz questions and choices'))
