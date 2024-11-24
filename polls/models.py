from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question=models.CharField(max_length=200)
    publish=models.DateTimeField("date published")

    def __str__(self):
        return self.question
    
    def wasPublishedRecently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.publish<=now



class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice