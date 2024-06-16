## Vishitiy.ua - project

---

### Information about our team
1. Danil
2. Olha
3. Oleksii
4. Vitalii


### Technologies and languages we used
1. Python
2. Django
2. JavaScript
3. HTML
4. CSS



### Libraries we used

```txt

asgiref==3.8.1
# 
crispy-bootstrap5==2024.2
# Библиотека для совместимости Django с Bootstrap5, упрощает создания форм с использованием Bootstrap5
django-crispy-forms==2.1
# Приложение Джанго которое помогает создавать красивые формы
sqlparse==0.5.0
# парсер для работы с базами данных SQL
Pillow==10.3.0 
# Библиотека для работы с изображениями
django-colorfield==0.11.0 
# Библиотека которая используется для добавления "выбора цвета или цветовых полей" в моделях джанго
django-filter==24.2
# Библиотека которая позволяет легко создавать фильтры для данных в приложении
mysqlclient==2.2.4
# Джанго использует для подключения и работ с базами данных
faker==25.8.0 
# генерация потдельных данных 
python-dateutil==2.9.0.post0 
# библиотека для работыы с датами и временем
six==1.16.0
# Предназначен для потдержки баз кода, которые работают как на Python 2 так и на Python 3
python-dotenv==1.0.1
""" 
считывает ключ-значение с файла .env и
может устанавливать их как переменные
(У нас в проекте используется для хранения конфиденциальных данных) )

"""
algoliasearch==3.0.0 
# Официальная библиотека клиента Алголия для пайтона, используется для взаимодействия с поисковыми системами Алголии 
algoliasearch==django-3.0.0
# Библиотека для интеграции Алголии с Джанго
certifi==2024.6.2
# 
charset-normalizer==3.3.2
# Библиотека, которая помогает вам читать текст из неизвестной кодировки.
idna==3.7
# Используется для работы с URL-адресами, содержащими не-ASCII символы.
requests==2.32.3 
# Библиотека используемая для выполнения HTTP запросов
urllib3==2.2.1
# Библиотека для работы с HTTP
django-countries==7.6.1
# Библиотека для Джанго которая позволяет использовать список стран в моделях и формах
typing-extensions==4.12.2
# 

```





#### Function in users app:

1. __functions for registration login and logout:__

```python
User = get_user_model()  # Получаем модель пользователя, используя функцию get_user_model

# Функция представления для регистрации нового пользователя
def signup_view(request):
    form = UserCreationForm()  
    # Создаем экземпляр стандартной формы UserCreationForm для регистрации пользователя
    if request.method == "POST":  
       # Если запрос метода POST
       form = UserCreationForm(request.POST)  
       # Используем данные POST для создания формы UserCreationForm
       if form.is_valid():  
           # Если данные формы прошли валидацию
           form.save()  
           # Сохраняем пользователя
           messages.success(request, "Аккаунт был успешно создан")  
           # Отправляем сообщение об успешном создании аккаунта
           return redirect("users:login")  
       # Перенаправляем пользователя на страницу входа
    return render(request, "registration/signup.html", {"form": form})  
# Отображаем шаблон signup.html с формой для регистрации пользователя

# Функция представления для входа пользователя в систему
def login_view(request):
    form = AuthenticationForm()  
    # Создаем экземпляр стандартной формы AuthenticationForm для входа пользователя
    if request.method == "POST":  
        # Если запрос метода POST
        form = AuthenticationForm(data=request.POST)  
        # Используем данные POST для создания формы AuthenticationForm
        if form.is_valid():  
            # Если данные формы прошли валидацию
            user = form.get_user()  
            # Получаем пользователя из формы аутентификации
            messages.success(request, f"Вы вошли как {user.username}")  
            # Отправляем сообщение о успешном входе пользователя
    return render(request, "registration/login.html", {"form": form})  
# Отображаем шаблон login.html с формой для входа пользователя

# Класс для представления выхода пользователя из системы
class LogoutView(DjangoLogoutView):
    http_method_names = ["post", "options", "get"]  
    # Указываем допустимые HTTP методы для этого представления
    def get(self, *args, **kwargs):  
        # Определяем метод GET
        if not self.request.user.is_authenticated:  
            # Если пользователь не аутентифицирован
            return redirect("users:login")  
        # Перенаправляем его на страницу входа
        return render(self.request, "registration/logout.html")  
    # Отображаем шаблон logout.html

# Класс для представления входа пользователя в систему
class LoginView(DjangoLoginView):
    redirect_authenticated_user = True  
    # Перенаправляем аутентифицированного пользователя
    form_class = forms.CustomAuthenticationForm  
    # Используем кастомную форму аутентификации CustomAuthenticationForm
    def form_valid(self, form):  
        # Переопределяем метод для обработки валидной формы
        messages.success(self.request, f"Вы вошли как {form.get_user().username}")  
        # Отправляем сообщение о успешном входе пользователя
        return super().form_valid(form)  
    # Вызываем родительский метод form_valid

# Класс для представления регистрации нового пользователя с использованием обобщенного представления CreateView
class SignupView(generic.CreateView):
    form_class = forms.CustomUserCreationForm  
    # Используем кастомную форму регистрации CustomUserCreationForm
    success_url = reverse_lazy("users:login")  
    # После успешной регистрации перенаправляем пользователя на страницу входа
    template_name = "registration/signup.html"  
    # Определяем имя шаблона для отображения формы регистрации
    def form_valid(self, form):  
        # Переопределяем метод для обработки валидной формы
        messages.success(self.request, "Аккаунт был успешно создан")  
        # Отправляем сообщение об успешной регистрации аккаунта
        return super().form_valid(form)  
    # Вызываем родительский метод form_valid для сохранения данных формы

```
_Этот код содержит представления для регистрации входа и выхода пользователя для этого мы использовали стандартные Джанго формы так же сдесь используем кастомные формы которы находятся в файле forms.py_

---

2.__Creat customs forms:__

```python

# создание кастомной формы аунтефикации наследующуюся от стандартных форм Джанго
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # Вызов родительского конструктора что бы инициализировать форму
        super().__init__(*args, **kwargs)
        # Если в данных формы ('self.data') есть поле password
        if 'password' in self.data:
            # Устанавливаем атрибут value виджета поля password равным значению из данных формы
            self.fields['password'].widget.attrs['value'] = self.data['password']

# создаём кастомную форму создания пользователя наследующуюся от стандартной формы создания пользователя Джанго
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # Вызов родительского конструктора что бы инициализировать форму
        super().__init__(*args, **kwargs)
        # Если в данных формы ('self.data') есть поле password1
        if 'password1' in self.data:
            # Устанавливаем атрибут 'value' виджета поля 'password1' равным значению из данных формы
            self.fields['password1'].widget.attrs['value'] = self.data['password1']
        # Если в данных формы ('self.data') есть поле password2
        if 'password2' in self.data:
            # Устанавливаем атрибут value виджета поля password2 равным значению из данных формы
            self.fields['password2'].widget.attrs['value'] = self.data['password2']

```

_Эти кастомные формы позволяют сохранять введённые пароли пользователем при перезагрузке страницы_

---


3.



---



