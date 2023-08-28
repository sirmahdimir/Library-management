from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    date_of_release = models.DateField()    
    price = models.DecimalField(max_digits=10, decimal_places=3)
    is_reserve = models.BooleanField()

    def __str__(self):
        return (f"Name: ~{self.title}~  / Author: ~{self.authors}~ / Reserve Status: ~{self.is_reserve}~")
    

    class Meta:
        db_table = "Books"