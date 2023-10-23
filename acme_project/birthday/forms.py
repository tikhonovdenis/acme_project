from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday

# class BirthdayForm(forms.Form):
#     first_name = forms.CharField(label='Имя', max_length=20)
#     last_name = forms.CharField(
#         label='Фамилия', required=False, help_text='Необязательное поле'
#     )
#     birthday = forms.DateField(
#         label='Дата рождения',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#     )

# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Чтобы форма работала как раньше — нужно указать, что для поля с датой рождения используется виджет с типом данных date
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
        # Указываем, что надо отобразить все поля.
        fields = '__all__'


# class ContestForm(forms.ModelForm):
#     class Meta:
#         model = Contest
#         widgets = {
#             'description': forms.Textarea({'cols': '22', 'rows': '5'}),
#             'comment': forms.Textarea({'cols': '22', 'rows': '5'})
#         }
#         fields = '__all__'