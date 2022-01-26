from time import time
from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return (self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #can this question be loosely used elsewhere to refer to Question e.g question.question_text to refer to question_text defined in the Question model
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return (self.choice_text)