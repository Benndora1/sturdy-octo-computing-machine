from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# admin
# 19949064

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True, null=True)
     
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices' ,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    

    def __str____(self):
        return self.choice_text
    
class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name='votes', on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User,  on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poll','voted_by')

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
