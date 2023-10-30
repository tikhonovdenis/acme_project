from django.db import models
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse

# Импортируется функция-валидатор.
from .validators import real_age


# from django.core.validators import MinValueValidator, MaxValueValidator
#
#
# class Contest(models.Model): title = models.CharField('Название', max_length=20) description = models.TextField(
# 'Описание') price = models.IntegerField('Цена', help_text='Рекомендованная розничная цена', validators=[
# MinValueValidator(10), MaxValueValidator(100)]) comment = models.TextField('Комментарий', blank=True)


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
