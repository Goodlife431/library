from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=265)
    date_of_birth = models.DateField()
    date_of_death = models.ForeignKey('Author', models.CASCADE())

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=55)
    isbn = models.CharField(max_length=13)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE())
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE())

    def __str__(self):
        return f"{self.title}----{self.date_added}"


class Genre(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=259)

    def __str__(self):
        return self.name



