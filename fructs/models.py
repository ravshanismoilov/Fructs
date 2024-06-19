from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class FromCountry(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'fromcountry'

    def __str__(self):
        return self.name


class Fructs(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    tn = models.IntegerField()
    fromcountry = models.ForeignKey(to=FromCountry, on_delete=models.SET_NULL, null=True)
    date_to_come = models.DateField()
    image = models.ImageField(upload_to='meva/', blank=True, null=True)

    class Meta:
        db_table = 'fructs'

    def __str__(self):
        return f'{self.name} {self.fromcountry} {self.date_to_come}'


class Review(models.Model):
    body = models.TextField()
    star_given = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    fruct = models.ForeignKey(to=Fructs, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    class Meta:
        db_table ='review'

    def __str__(self):
        return f'{self.fruct.name} - {self.star_given} - {self.user}'