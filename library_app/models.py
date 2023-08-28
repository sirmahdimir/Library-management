from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    date_of_release = models.DateField()    
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
    

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     city = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name + '' + self.last_name

    
    
# class Borrow(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     borrow_date = models.DateField()
#     return_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.book.title}"