from django.db import models

# Create your models here.

# create an advertisement model so that advertisements can be retrieved from the DB

class Advertisement(models.Model):
    name = models.CharField(max_length=200, null=True)
    logo = models.ImageField(upload_to='static/spoonsers/')
    ad_link = models.URLField()
    ad_text = models.TextField(max_length=1000)

    # def __str__(self):
    #     return '{}'.format(self.name) # displays the company name on the Admin side rather than 'Advertisement Object(X)'
    