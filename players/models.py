from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
from django_countries.fields import CountryField

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    birthdate = models.DateField(null=True, blank=True, verbose_name='Год Рождения')
    club = models.CharField(max_length=150, verbose_name='Клуб')
    photo = models.ImageField(upload_to = 'photos/%Y/%m%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    height = models.IntegerField(verbose_name='Рост')
    citizenship = CountryField(multiple=True)
    born_place = models.CharField(max_length=150, verbose_name='Место Рождения')
    price = MoneyField(max_digits=14, decimal_places=1, default_currency='USD',verbose_name='Цена в Transfermarkt' )
    foots = [
        ('Правая', 'правая'),
        ('Левая', 'левая'),
        ('Обе', 'обе'),
    ]
    national_matches = models.IntegerField(default=0, verbose_name="Матчи за сборную", blank=True)
    national_goals = models.IntegerField(default=0, verbose_name="голы за сборную", blank=True)
    national_assists = models.IntegerField(default=0, verbose_name="голевые за сборную", blank=True)
    foot = models.CharField(max_length=150, choices = foots, verbose_name='Рабочая нога')
    chempionship = models.CharField(max_length=150, verbose_name='Чемпионат', blank=True)
    matches_chempionship = models.IntegerField(default=0, verbose_name="Матчи в чемпионате", blank=True)
    goals_chempionship = models.IntegerField(default=0, verbose_name="Голы в чемпионате", blank=True)
    assists_chempionship = models.IntegerField(default=0, verbose_name="Голевые в чемпионате", blank=True)
    cup_name = models.CharField(max_length=150, verbose_name='Кубок', default='', blank=True)
    matches_cup = models.IntegerField(default=0, verbose_name="Матчи в кубке", blank=True)
    goals_cup = models.IntegerField(default=0, verbose_name="Голы в кубке", blank=True)
    assists_cup = models.IntegerField(default=0, verbose_name="Голевые в кубке", blank=True)
    international_cup = models.CharField(max_length=150, verbose_name='Международный турнир', default='', blank=True)
    matches_international = models.IntegerField(default=0, verbose_name="Матчи в еврокубках", blank=True, null=True)
    goals_international = models.IntegerField(default=0, verbose_name="Голы в еврокубках", blank=True, null=True)
    assists_international = models.IntegerField(default=0, verbose_name="голевые в еврокубках", blank=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single_player', kwargs={"slug": self.slug})

    class Meta:
            ordering = ['-price']
            verbose_name = 'Футболисты'
            verbose_name_plural = 'Футболисты'
