from django.db import models

# Create your models here.
class Buyer(models.Model):
    '''
    покупатели
    '''
    name = models.CharField(max_length=20, unique=True)  # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс(DecimalField)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    '''
    игра
    '''
    title = models.CharField(max_length=50,unique=True) #название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2) #цена(DecimalField)
    size = models.DecimalField(max_digits=10, decimal_places=2) #размер файлов игры(DecimalField)
    description = models.TextField(blank=True) #описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False) #ограничение возраста 18+ (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='games')#покупатель обладающий игрой (ManyToManyField). У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.

    def __str__(self):
        return self.title


