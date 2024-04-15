from django.db import models

# Create your models here.
class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=200)

class QuizChoice(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
