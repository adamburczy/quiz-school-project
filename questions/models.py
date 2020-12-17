from django.db import models

class Question(models.Model):
    correct_answear = models.IntegerField(default=0) #random?

