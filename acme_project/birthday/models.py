# Да, именно так всегда и ссылаемся на модель пользователя!
from django.contrib.auth import get_user_model
from django.db import models
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse

# Импортируется функция-валидатор.
from .validators import real_age

# Да, именно так всегда и ссылаемся на модель пользователя!
User = get_user_model()


# from django.core.validators import MinValueValidator, MaxValueValidator
#
#
# class Contest(models.Model): title = models.CharField('Название', max_length=20) description = models.TextField(
# 'Описание') price = models.IntegerField('Цена', help_text='Рекомендованная розничная цена', validators=[
# MinValueValidator(10), MaxValueValidator(100)]) comment = models.TextField('Комментарий', blank=True)

class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)

    def __str__(self):
        return self.tag


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    )

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


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
