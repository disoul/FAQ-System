from django.db import models



# User (name, email,password)
class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return """
        name: {}
        email: {}
        password: {}
        """.format(self.name, self.email, self.password)


# Question (title,user,answers,date)
class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=20, unique=True)
    content = models.CharField(max_length=10000)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return """
        user: {}
        title: {}
        content: {}
        date: {}
        """.format(self.user.name, self.title, self.content, self.date)


# Answer (content,user,date)
class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    content = models.CharField(max_length=10000)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return """
        user: {}
        question: {}
        content: {}
        date: {}
        """.format(self.user.name, self.question.title, self.content, self.date)
