from django.db import models

# Create your models here.\

class Book(models.Model):


    name = models.CharField(max_length=20,verbose_name='书名')
    price = models.IntegerField()
    pub_date = models.DateField()
    #作者
    author = models.ManyToManyField("Author")
    #出版社
    publish = models.ForeignKey("Publish")

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)

    def __str__(self):

        return self.name


class Publish(models.Model):

    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name


