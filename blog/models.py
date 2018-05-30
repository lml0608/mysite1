from django.db import models

# Create your models here.\

class Book(models.Model):


    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    #作者
    #author = models.ForeignKey("Author")
    #出版社
    publish = models.ForeignKey("Publish")


class Author(models.Model):

    name = models.CharField(max_length=32)


class Publish(models.Model):

    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)



