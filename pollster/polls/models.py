from django.db import models

# Create your models here (like tables in a database)

class Question(models.Model):
    #specify fields (primary key by default, autoincremented
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):   #not to display 'Question Object'
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #delete choice if questions gets deleted
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text