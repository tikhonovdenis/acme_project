from django import forms
# Импортируем класс ошибки валидации.
from django.core.exceptions import ValidationError
# Импорт функции для отправки почты.
from django.core.mail import send_mail

# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation

# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


# class ContestForm(forms.ModelForm):
#     class Meta:
#         model = Contest
#         widgets = {
#             'description': forms.Textarea({'cols': '22', 'rows': '5'}),
#             'comment': forms.Textarea({'cols': '22', 'rows': '5'})
#         }
#         fields = '__all__'

# class BirthdayForm(forms.Form):
#     first_name = forms.CharField(label='Имя', max_length=20)
#     last_name = forms.CharField(
#         label='Фамилия', required=False, help_text='Необязательное поле'
#     )
#     birthday = forms.DateField(
#         label='Дата рождения',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#     )

# Для использования формы с моделями меняем класс на forms. ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Чтобы форма работала как раньше — нужно указать, что для поля с датой рождения используется виджет с типом
        # данных date
        exclude = ('author',)
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}
        # Указываем, что надо отобразить все поля.
        fields = '__all__'

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        # Вызов родительского метода clean.
        super().clean()
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            # Отправляем письмо, если кто-то представляется
            # именем одного из участников Beatles.
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError('Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!')


class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ('text',)
