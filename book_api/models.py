from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    number_of_pages = models.IntegerField()
    pub_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
