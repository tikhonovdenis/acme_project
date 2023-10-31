# Импортируем настройки проекта.
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
from django.contrib import admin

# Добавьте новые строчки с импортами классов.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

...
# К импортам из django.urls добавьте импорт функции reverse_lazy
from django.urls import include, path, reverse_lazy

urlpatterns = [
                  path('', include('pages.urls')),
                  path('admin/', admin.site.urls),
                  path('birthday/', include('birthday.urls')),
                  path(
                      'auth/registration/',
                      CreateView.as_view(
                          template_name='registration/registration_form.html',
                          form_class=UserCreationForm,
                          success_url=reverse_lazy('pages:homepage'),
                      ),
                      name='registration',
                  ),
                  path('auth/', include('django.contrib.auth.urls')),  # Подключаем urls.py приложения для работы с
                  # пользователями и В конце добавляем к списку вызов функции static.
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
