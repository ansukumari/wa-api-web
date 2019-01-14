from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    # from django.utils import timezone
    # q = Question(question_text="What's new?", pub_date=timezone.now())


    @property
    def duration(self):
        pass 

    def __str__(self):
        return self.name


class Creative(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=200)
    media_link = models.CharField(max_length=200)
    sending_no = models.CharField(max_length=200)
    no_dp = models.CharField(max_length=200)

class Client(models.Model):
    phone_no = models.CharField(max_length=200)
    campaigns = models.ManyToManyField(Campaign)

    def __str__(self):
        return self.phone_no

