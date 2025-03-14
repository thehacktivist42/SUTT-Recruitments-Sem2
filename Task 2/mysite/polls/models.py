from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    def __str__(self):
        return self.questionText
    def wasPublishedRecently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days = 1)
    questionText = models.CharField("Question Text", max_length = 200)
    pubDate = models.DateTimeField("Date Published")

class Choice(models.Model):
    def __str__(self):
        return self.choiceText
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choiceText = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
