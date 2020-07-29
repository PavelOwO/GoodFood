from django.db import models


class Food(models.Model):
    image = models.ImageField("Image of food")
    food_name = models.CharField("Name of the dish", max_length=30)
    discription = models.TextField("Food discription")
    price = models.IntegerField("Food price $")

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'


class Rate(models.Model):
    ratings = models.ForeignKey(Food, on_delete=models.CASCADE)
    author_name = models.CharField("Author's name", max_length=30)
    author_rate = models.IntegerField("Author's rate")

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'
