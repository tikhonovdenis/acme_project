from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Получаем модель пользователя:
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # Наследуем класс Meta от соответствующего класса родительской формы.
    # Так этот класс будет не перезаписан, а расширен.
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'bio')
