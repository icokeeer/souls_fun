from django.db import models


class SoulsText(models.Model):
    souls_text = models.CharField(max_length=500)
    like_counts = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.souls_text
