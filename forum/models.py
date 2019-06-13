from django.db import models
from oauth.models import User
from tinymce import HTMLField
from elasticsearchapp.search import QuestionsIndex

class Questions(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=140)
    description     = HTMLField()
    num_replies     = models.IntegerField(default=0)
    date_published  = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def indexing(self):
        obj = QuestionsIndex(
            meta={'id': self.id},
            question_id = self.id,
            num_replies = self.num_replies,
            title=self.title,
            date_published=self.date_published,
        )
        obj.save()
        return obj.to_dict(include_meta=True)


class Answers(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    question        = models.ForeignKey(Questions,on_delete=models.CASCADE)
    reply           = HTMLField()
    date_published  = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.reply

class Notifications(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    message         = models.CharField(max_length=100)
    read            = models.BooleanField(default=False)
    notif_date      = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.message