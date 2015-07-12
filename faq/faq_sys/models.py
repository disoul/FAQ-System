from django.db import models

# User (name, email,password)
class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

# Question (title,user,date)
class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=20, unique=True)
    content = models.CharField(max_length=200)
    date = models.DateField()

# Answer (content,user,date)
class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    date = models.DateField()
