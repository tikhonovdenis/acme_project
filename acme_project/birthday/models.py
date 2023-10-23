from django.db import models

# from django.core.validators import MinValueValidator, MaxValueValidator
#
#
# class Contest(models.Model):
#     title = models.CharField('Название', max_length=20)
#     description = models.TextField('Описание')
#     price = models.IntegerField('Цена', help_text='Рекомендованная розничная цена', validators=[MinValueValidator(10), MaxValueValidator(100)])
#     comment = models.TextField('Комментарий', blank=True)


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения')


