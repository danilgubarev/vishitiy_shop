# Vishitiy.ua - project

_Our project is a online store for selling clothes_

---

### DIFFERENT INFORMATION 

- [How use it](#how-use-it)

- [Information about our team](#information-about-our-team)

- [Our project structure](#our-project-structure)

- [Technologies and languages we used](#technologies-and-languages-we-used)

- [Libraries we used](#libraries-we-used)

### ALL OUR APPS

- [USERS APP](#users-app)

- [PRODUCTS APP](#products-app)

- [CART APP](#cart-app)

- [MAIN APP](#main-app)

- [APP YOUR DESIGN](#app-your-design)

- [APP PAYMENTS](#app-payments)

### OUR CONTACTS

- [CONTACTS](#contacts)

---

# How use it

1. >git clone https://github.com/danilgubarev/vishitiy_shop.git
2. >pip install -r requirements.txt
3. >npm install
4. >npm run dev
5. >python manage.py runserver

---

# Information about our team
1. GitHub - [Danil](https://github.com/danilgubarev)
2. GitHub - [Olha](https://github.com/Olhabd)
3. GitHub - [Oleksii](https://github.com/AlexeyTarasov77)
4. GitHub - [Vitalii](https://github.com/IWaithI)

---

1. Figma - [Danil](https://www.figma.com/design/kITnzVDamIAVnLsSdZr3VM/vishitiy?node-id=0-1&t=gEzSZBI2PThBR6iK-1)
2. Figma - [Olha](https://www.figma.com/design/kITnzVDamIAVnLsSdZr3VM/vishitiy?t=YzVNAU0GbcKXdTTA-0)
3. Figma - [Oleksii](https://www.figma.com/design/TfGbzNcv8RlRhQKjstFQ0e/Design?node-id=0-1&t=9oRZAN8ghNfeRUgZ-1)
4. Figma - [Vitalii](https://www.figma.com/design/v19cj5mrLwEPN9hKKdGXYQ/Untitled?node-id=0-1&t=9zSuZg68wKwLJrJa-1)


---

# Our project structure

```mermaid
graph TD

  C{VISHITIY_SHOP}
  C -->|main| A[use for create main page] --> 1(views.py) --> 2(mixins.py)
  C -->|cart| B[use for create cart] --> 4(views.py) --> 5(cart.py) --> 6(forms.py)
  C -->|products| M[use for create pages list products and detail] --> 7(views.py) --> 8(models.py) --> 9(filters.py) --> l(admin.py)
  C -->|your_design| D[use for create page your design] --> 0(views.py)
  C -->|users| E[use for create auth/reg and logout] --> e(views.py) --> t(forms.py)
  C -->|payments| F[ for create form for submit order] --> z(views.py) -->  c(forms.py)


```
---


# Technologies and languages we used
1. >Python/Django - We used Python and Django for rapid development of web applications.
2. >JavaScript -  We used JavaScript for managing the item counter, displaying popup notifications, and interacting with the shopping cart.
3. >HTML - We used HTML for structuring our website.
4. >CSS - We used CSS for styling our website.
5. >MySQL - We use MySQL to store various data about products and users.
6. >sqlite3 - We used sqlite3 to store various data about products and users.
6. >Bootstrap - We used Bootstrap for its classes and templates, as well as for implementing responsiveness.
7. >Figma - We used Figma for creating the design of our website.   
8. >jQuery/Ajax - We use jQuery/Ajax to prevent full page reload when submitting a form or adding an item to the cart.



## Libraries we used

```txt

asgiref==3.8.1
# Library for ASGI reference implementation, necessary for Django's async support
# Бібліотека для реалізації ASGI, необхідна для асинхронної підтримки Django

crispy-bootstrap5==2024.2
# Library for Django compatibility with Bootstrap5, simplifies the creation of forms using Bootstrap5
# Бібліотека для сумісності Django з Bootstrap5, спрощує створення форм з використанням Bootstrap5

Django==5.0.6
# Framework for building web applications
# Фреймворк для створення веб-застосунків

django-crispy-forms==2.1
# Django application that helps create beautiful forms
# Застосунок Django, який допомагає створювати гарні форми

sqlparse==0.5.0
# Parser for working with SQL databases
# Парсер для роботи з базами даних SQL

Pillow==10.3.0
# Library for working with images
# Бібліотека для роботи з зображеннями

django-colorfield==0.11.0
# Library used to add "color picker or color fields" in Django models
# Бібліотека, що використовується для додавання "вибору кольору або кольорових полів" у моделях Django

django-filter==24.2
# Library that allows easy creation of filters for data in applications
# Бібліотека, яка дозволяє легко створювати фільтри для даних у застосунках

mysqlclient==2.2.4
# Used by Django for connecting to and working with databases
# Використовується Django для підключення та роботи з базами даних

faker==25.8.0
# Library for generating fake data
# Бібліотека для генерації фальшивих даних

python-dateutil==2.9.0.post0
# Library for working with dates and times
# Бібліотека для роботи з датами та часом

six==1.16.0
# Utility library for supporting code that works on both Python 2 and Python 3
# Бібліотека для підтримки коду, який працює як на Python 2, так і на Python 3

python-dotenv==1.0.1
# Library for loading environment variables from a .env file
# Бібліотека для завантаження змінних середовища з файлу .env
# Reads key-value pairs from a .env file and can set them as environment variables
# Зчитує ключ-значення з файлу .env і може встановлювати їх як змінні середовища
# (Used in the project to store confidential data)
# (У нашому проєкті використовується для зберігання конфіденційних даних)

algoliasearch==3.0.0
# Official Algolia client library for Python, used for interacting with Algolia search systems
# Офіційна бібліотека клієнта Algolia для Python, використовується для взаємодії з пошуковими системами Algolia

algoliasearch-django==3.0.0
# Library for integrating Algolia with Django
# Бібліотека для інтеграції Algolia з Django

certifi==2024.6.2
# Python package for providing Mozilla's CA Bundle
# Пакет Python для надання CA Bundle від Mozilla

charset-normalizer==3.3.2
# Library that helps you read text from unknown encoding
# Бібліотека, яка допомагає читати текст з невідомого кодування

idna==3.7
# Used for handling internationalized domain names (IDNs)
# Використовується для роботи з URL-адресами, що містять не-ASCII символи

requests==2.32.3
# Library used for making HTTP requests
# Бібліотека, що використовується для виконання HTTP-запитів

urllib3==2.2.1
# HTTP client library
# Бібліотека для роботи з HTTP

django-countries==7.6.1
# Django library that provides a country field for models and forms
# Бібліотека Django, яка дозволяє використовувати список країн у моделях і формах

typing-extensions==4.12.2
# Backported and experimental type hints for Python
# Пакет із додатковими анотаціями типів для Python

```

---

# USERS APP

---

### VIEWS.PY

1. __functions for registration login and logout:__

```python
User = get_user_model()  # Getting the user model using the get_user_model function / Отримуємо модель користувача за допомогою функції get_user_model

# View function for registering a new user / Функція представлення для реєстрації нового користувача
def signup_view(request):
    form = UserCreationForm()  # Creating an instance of the standard UserCreationForm for user registration / Створюємо екземпляр стандартної форми UserCreationForm для реєстрації користувача
    if request.method == "POST":  # If the request method is POST / Якщо запит методу POST
       form = UserCreationForm(request.POST)  # Using POST data to create the UserCreationForm / Використовуємо дані POST для створення форми UserCreationForm
       if form.is_valid():  # If the form data is valid / Якщо дані форми пройшли валідацію
           form.save()  # Saving the user / Зберігаємо користувача
           messages.success(request, "Account successfully created")  # Sending a success message about the account creation / Відправляємо повідомлення про успішне створення облікового запису
           return redirect("users:login")  # Redirecting the user to the login page / Перенаправляємо користувача на сторінку входу
    return render(request, "registration/signup.html", {"form": form})  # Displaying the signup.html template with the user registration form / Відображаємо шаблон signup.html з формою для реєстрації користувача

# View function for user login / Функція представлення для входу користувача
def login_view(request):
    form = AuthenticationForm()  # Creating an instance of the standard AuthenticationForm for user login / Створюємо екземпляр стандартної форми AuthenticationForm для входу користувача
    if request.method == "POST":  # If the request method is POST / Якщо запит методу POST
        form = AuthenticationForm(data=request.POST)  # Using POST data to create the AuthenticationForm / Використовуємо дані POST для створення форми AuthenticationForm
        if form.is_valid():  # If the form data is valid / Якщо дані форми пройшли валідацію
            user = form.get_user()  # Getting the user from the authentication form / Отримуємо користувача з форми аутентифікації
            messages.success(request, f"You are logged in as {user.username}")  # Sending a success message about the user's login / Відправляємо повідомлення про успішний вхід користувача
    return render(request, "registration/login.html", {"form": form})  # Displaying the login.html template with the login form / Відображаємо шаблон login.html з формою для входу користувача

# Class for handling user logout / Клас для обробки виходу користувача
class LogoutView(DjangoLogoutView):
    http_method_names = ["post", "options", "get"]  # Specifying allowed HTTP methods for this view / Вказуємо дозволені HTTP-методи для цього представлення
    def get(self, *args, **kwargs):  # Defining the GET method / Визначаємо метод GET
        if not self.request.user.is_authenticated:  # If the user is not authenticated / Якщо користувач не аутентифікований
            return redirect("users:login")  # Redirecting them to the login page / Перенаправляємо його на сторінку входу
        return render(self.request, "registration/logout.html")  # Displaying the logout.html template / Відображаємо шаблон logout.html

# Class for handling user login using Django's built-in LoginView / Клас для обробки входу користувача за допомогою вбудованого LoginView у Django
class LoginView(DjangoLoginView):
    redirect_authenticated_user = True  # Redirecting authenticated users / Перенаправлення аутентифікованих користувачів
    form_class = forms.CustomAuthenticationForm  # Using a custom authentication form CustomAuthenticationForm / Використовуємо спеціальну форму автентифікації CustomAuthenticationForm
    def form_valid(self, form):  # Overriding method to handle valid form submission / Перевизначення методу для обробки валідних даних форми
        messages.success(self.request, f"You are logged in as {form.get_user().username}")  # Sending a success message about the user's login / Відправляємо повідомлення про успішний вхід користувача
        return super().form_valid(form)  # Calling the parent method form_valid for form data saving / Викликаємо батьківський метод form_valid для збереження даних форми

# Class for user registration using generic CreateView / Клас для реєстрації користувача за допомогою загального представлення CreateView
class SignupView(generic.CreateView):
    form_class = forms.CustomUserCreationForm  # Using a custom registration form CustomUserCreationForm / Використовуємо спеціальну форму реєстрації CustomUserCreationForm
    success_url = reverse_lazy("users:login")  # Redirecting the user to the login page after successful registration / Перенаправлення користувача на сторінку входу після успішної реєстрації
    template_name = "registration/signup.html"  # Specifying the template name for displaying the registration form / Вказуємо ім'я шаблону для відображення форми реєстрації
    def form_valid(self, form):  # Overriding method to handle valid form submission / Перевизначення методу для обробки валідних даних форми
        messages.success(self.request, "Account successfully created")  # Sending a success message about the account registration / Відправляємо повідомлення про успішну реєстрацію облікового запису
        return super().form_valid(form)  # Calling the parent method form_valid to save form data / Викликаємо батьківський метод form_valid для збереження даних форми


```
* >This code contains views for user login and logout functionalities. We used standard Django forms, as well as custom forms located in the forms.py file.
* >Цей код містить представлення для входу та виходу користувача. Ми використовували стандартні форми Django, а також кастомні форми, які знаходяться у файлі forms.py.

### FORMS.PY

2.__Creat customs forms:__

```python

# Creating a custom authentication form inheriting from Django's standard forms
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # Calling the parent constructor to initialize the form / Виклик батьківського конструктора для ініціалізації форми
        super().__init__(*args, **kwargs)
        # If 'password' field is present in form data ('self.data') / Якщо поле 'password' є в даних форми ('self.data')
        if 'password' in self.data:
            # Setting the 'value' attribute of the password field widget to the value from form data / Встановлення атрибуту 'value' віджета поля пароля на значення з даних форми
            self.fields['password'].widget.attrs['value'] = self.data['password']

# Creating a custom user creation form inheriting from Django's standard UserCreationForm / Створення власної форми створення користувача, що успадковується від стандартної UserCreationForm Django
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # Calling the parent constructor to initialize the form / Виклик батьківського конструктора для ініціалізації форми
        super().__init__(*args, **kwargs)
        # If 'password1' field is present in form data ('self.data') / Якщо поле 'password1' є в даних форми ('self.data')
        if 'password1' in self.data:
            # Setting the 'value' attribute of the 'password1' field widget to the value from form data / Встановлення атрибуту 'value' віджета поля 'password1' на значення з даних форми
            self.fields['password1'].widget.attrs['value'] = self.data['password1']
        # If 'password2' field is present in form data ('self.data') / Якщо поле 'password2' є в даних форми ('self.data')
        if 'password2' in self.data:
            # Setting the 'value' attribute of the 'password2' field widget to the value from form data / Встановлення атрибуту 'value' віджета поля 'password2' на значення з даних форми
            self.fields['password2'].widget.attrs['value'] = self.data['password2']







```

_These custom forms allow saving user-entered passwords even when the page is refreshed./Ці кастомні форми дозволяють зберігати введені користувачем паролі навіть при перезавантаженні сторінки._

---


# PRODUCTS APP

---

### VIEWS.PY

1. __Displaying a list of products, as well as product details (personal product page)__




```python 

class ProductListView(generic.ListView):
    # Here we specify the template to be used for displaying the list of products / Тут ми вказуємо шаблон, який буде використовуватись для відображення списку продуктів
    template_name = 'products/product_list.html'
    # Set the queryset to retrieve all Product objects and use select_related for query optimization / Встановлюємо queryset для отримання всіх об'єктів Product і використання select_related для оптимізації запитів
    queryset = Product.objects.all().select_related("collection")

    # Method to get the queryset / Метод для отримання queryset
    def get_queryset(self) -> QuerySet[Product]:
        # Call get_queryset from the parent class to get the base queryset / Викликаємо get_queryset з батьківського класу, щоб отримати базовий queryset
        qs = super().get_queryset()
        # Create an instance of the filter, passing GET request parameters and the base queryset / Створюємо екземпляр фільтра, передаючи параметри GET запиту і базовий queryset
        self.filterset = ProductFilter(self.request.GET, queryset=qs)
        # Return the filtered queryset / Повертаємо відфільтрований queryset
        return self.filterset.qs
    
    # Method to get the context data that will be passed to the template / Метод для отримання контекстних даних, які будуть передані в шаблон
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # Get the base context from the parent class / Отримуємо базовий контекст з батьківського класу
        context = super().get_context_data(**kwargs)
        # Add the filter form to the context / Додаємо форму фільтра до контексту
        context["form"] = self.filterset.form
        # Return the context / Повертаємо контекст
        return context


class ProductDetailView(generic.DetailView):
    # Set the queryset to retrieve all Product objects and use select_related for query optimization / Встановлюємо queryset для отримання всіх об'єктів Product і використання select_related для оптимізації запитів
    queryset = Product.objects.all().select_related("collection")
    # Specify the template to be used for displaying the product details / Вказуємо шаблон, який буде використовуватись для відображення деталей продукту
    template_name = "products/product_detail.html"


```

<<<<<<< HEAD


* >ProductListView - відображає весь список продуктів з використанням фільтрації.
* >ProductDetailView - відображає особисту сторінку товару.

* >Ці класи використовуються у Django для керування видами: generic.ListView для відображення списку об'єктів моделі і generic.DetailView для відображення детальної інформації про продукт (сторінка індивідуального продукту)._

* >generic.ListView - використовується для відображення списку об'єктів моделі у Django.
* >generic.DetailView - використовується для відображення детальної інформації про конкретний продукт (особиста сторінка продукту).


### MODELS.PY

2. Creating Product and Collection Models

```python
class Product(SaveSlugMixin, models.Model):
    # Define the Product model inheriting from SaveSlugMixin and models.Model / Визначення моделі Product, що успадковує SaveSlugMixin та models.Model
    ACCEPTABLE_SIZES = ["XS", "S", "M", "L", "XL", "XXL"]  
    # Допустимі розміри продукту
    SIZE_CHOICES = tuple((size, size) for size in ACCEPTABLE_SIZES)  
    # Створюємо кортеж з варіантами розмірів для вибору
    COLOR_PALETTE = tuple((color, color) for color in ("white", "black", "red", "green", "blue", "yellow"))  
    # Кольорова палітра
    PRODUCT_TYPE_CHOICES = tuple(
        (type, type)
        for type in ("shoes", "t-shirt", "sweatshirt", "pants", "jacket", "sunglasses")  # Варіанти типів продуктів
    )
    
    SIZE_VALIDATOR = ProductSizeValidator(ACCEPTABLE_SIZES)  
    # Створюємо екземпляр валідатора розмірів
    
    title = models.CharField(max_length=150)  
    # Поле для назви продукту
    slug = models.SlugField(unique=True, blank=True)  
    # Поле для slug, унікальне і може бути пустим
    available_colors = models.JSONField(default=list)  
    # Поле для доступних кольорів, використовується JSON
    available_sizes = models.JSONField(default=list, validators=[SIZE_VALIDATOR.validate_size])  
    # Поле для доступних розмірів, використовується JSON з валідатором
    available = models.BooleanField(default=True)  
    # Поле для статусу доступності продукту
    type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=50)  
    # Поле для типу продукту з обмеженим вибором
    image = models.ImageField()  
    # Поле для зображення продукту
    description = models.TextField(blank=True, null=True)  
    # Поле для опису продукту, може бути пустим або null
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    # Поле для ціни продукту
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]  
        # Поле для знижки з валідаторами мінімального та максимального значення
    )
    collection = models.ForeignKey(
        "Collection", on_delete=models.CASCADE, related_name="products"  
        # Поле зовнішнього ключа, зв'язує продукт з колекцією
    )

    def __str__(self) -> str:
        return self.title  
    # Метод для рядкового представлення об'єкта
    
    @property
    def image_url(self):
        return self.image.url  
    # Властивість для отримання URL зображення
    
    @property
    def final_price(self):
        return self.price - (self.price * self.discount / 100)  
    # Властивість для обчислення кінцевої ціни з урахуванням знижки

    @property
    def url(self):
        return self.get_absolute_url()  
    # Властивість для отримання абсолютного URL продукту
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})  
    # Метод для отримання абсолютного URL продукту
    
    def save(self, *args, **kwargs) -> None:
        return super().save(slugify_value=self.title, *args, **kwargs)  
    # Метод для збереження об'єкта з автоматичним генеруванням slug

class Collection(SaveSlugMixin, models.Model):
    # Define the Collection model inheriting from SaveSlugMixin and models.Model / Визначення моделі Collection, що успадковує SaveSlugMixin та models.Model
    name = models.CharField(max_length=150)  
    # Поле для назви колекції
    slug = models.SlugField(unique=True, blank=True)  
    # Поле для slug, унікальне і може бути пустим
    image = models.ImageField()  
    # Поле для зображення колекції
    description = models.TextField(blank=True, null=True)  
    # Поле для опису колекції, може бути пустим або null

    def __str__(self) -> str:
        return self.name  
    # Метод для рядкового представлення об'єкта

    def save(self, *args, **kwargs) -> None:
        return super().save(slugify_value=self.name, *args, **kwargs)  
    # Метод для збереження об'єкта з автоматичним генеруванням slug


```


* >This code is used to work with Collections and Products, providing convenient methods for accessing, saving, and linking data in the database.
* >Цей код використовується для роботи з Колекціями та Товарами, забезпечуючи зручні методи доступу, збереження та зв'язування даних в базі даних.

* >@property - representing a method as an object property./ дозволяє представляти метод як властивість об'єкта.


### FILTERS.PY


3. Filtering data on a page

```python

# Define the filter class for the Product model / Визначення класу фільтра для моделі Product
class ProductFilter(django_filters.FilterSet):
    # Price filter using a custom range widget / Фільтр ціни з використанням власного виджету діапазону цін
    price = django_filters.RangeFilter(widget=CustomRangeWidget(attrs={'class': 'px-3 py-2 border border-gray-200 rounded w-24 text-center'}))
    
    # Size filter using a multiple choice widget with checkboxes / Фільтр розміру з використанням віджета множинного вибору з прапорцями
    size = django_filters.TypedMultipleChoiceFilter(
        field_name="available_sizes",  # Model field for filtering / Поле моделі для фільтрації
        choices=Product.SIZE_CHOICES,  # Available size options / Доступні варіанти розмірів
        widget=forms.CheckboxSelectMultiple,  # Widget to display options as checkboxes / Віджет для відображення варіантів у вигляді прапорців
        lookup_expr='icontains'  # Lookup expression (case-insensitive substring search) / Вираз пошуку (пошук підстроки без урахування регістру)
    )
    
    # Collection filter using a multiple choice widget with checkboxes / Фільтр колекції з використанням віджета множинного вибору з прапорцями
    collection = django_filters.ModelMultipleChoiceFilter(
        queryset=Collection.objects.all(),  # All collection objects / Усі об'єкти колекції
        widget=forms.CheckboxSelectMultiple  # Widget to display options as checkboxes / Віджет для відображення варіантів у вигляді прапорців
    )
    
    # Color filter using a multiple choice widget with checkboxes / Фільтр кольору з використанням віджета множинного вибору з прапорцями
    color = django_filters.TypedMultipleChoiceFilter(
        field_name='available_colors',  # Model field for filtering / Поле моделі для фільтрації
        choices=Product.COLOR_PALETTE,  # Available color options / Доступні варіанти кольорів
        widget=forms.CheckboxSelectMultiple,  # Widget to display options as checkboxes / Віджет для відображення варіантів у вигляді прапорців
        lookup_expr='icontains'  # Lookup expression (case-insensitive substring search) / Вираз пошуку (пошук підстроки без урахування регістру)
    )
    
    # Filter to display only discounted products using a checkbox widget / Фільтр для відображення лише продуктів із знижкою з використанням віджета прапорця
    discounted_only = django_filters.BooleanFilter(
        field_name="discount",  # Model field for filtering / Поле моделі для фільтрації
        label="Discounted only",  # Filter label / Мітка фільтра
        widget=forms.CheckboxInput,  # Widget to display as checkbox / Віджет для відображення у вигляді прапорця
        method='filter_discounted_only'  # Method to filter / Метод для фільтрації
    )
    
    # Filtering method to return only discounted products when the checkbox is selected / Метод фільтрації, що повертає лише продукти із знижкою, якщо вибрано прапорець
    def filter_discounted_only(self, queryset, name, value):
        if value:  # If the checkbox is selected / Якщо вибрано прапорець
            return queryset.filter(discount__gt=0)  # Return products with non-zero discount / Повертаємо продукти з ненульовою знижкою
        return queryset  # Otherwise, return all products / В іншому випадку повертаємо всі продукти

    # Meta class to specify the model and fields used for filtering / Метаклас для вказівки моделі та полів, які використовуються для фільтрації
    class Meta:
        model = Product  # Specify the model for which the filter is created / Вказуємо модель, для якої створюється фільтр
        fields = ["price", "discounted_only", "type", "size", "color", "collection"]  # Fields of the model used for filtering / Поля моделі, які використовуються для фільтрації



```

<<<<<<< HEAD
* >This code performs filtering on the page based on various parameters such as price, product type, size, color, collection, etc.
* >Цей код здійснює фільтрацію на сторінці за різними параметрами, такими як ціна, тип продукту, розмір, колір, колекція і т. д.

### ADMIN.PY

3. Customization of the admin panel
_This code performs filtering on the page based on various parameters such as price, product type, size, color, collection, etc./Цей код здійснює фільтрацію на сторінці за різними параметрами, такими як ціна, тип продукту, розмір, колір, колекція і т. д._

___


3. Кастомизация админ панели


```python
# Register the Collection model in the admin panel / Реєстрація моделі Collection у панелі адміністратора
admin.site.register(Collection)

# Register the Product model using a custom ProductAdmin class / Реєстрація моделі Product з використанням кастомного класу ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the list of products in the admin panel / Поля, які будуть відображатися у списку продуктів у панелі адміністратора
    list_display = ["title", "final_price", "collection", "available"]
    
    # Override the get_form method to customize the product editing form / Перевизначення методу get_form для кастомізації форми редагування продукту
    def get_form(self, request, obj=None, **kwargs):
        # Get the base form for the Product model / Отримуємо базову форму для моделі Product
        form = super().get_form(request, obj, **kwargs)
        
        # Customize the widget for the available_sizes field / Кастомізація віджета для поля available_sizes
        form.base_fields['available_sizes'].widget = forms.CheckboxSelectMultiple(
            choices=Product.SIZE_CHOICES,  # Set the available size options / Встановлюємо доступні варіанти розмірів
            attrs={'class': 'form-control'},  # Add CSS class for styling / Додаємо CSS-клас для стилізації
        )
        
        # Customize the widget for the available_colors field / Кастомізація віджета для поля available_colors
        form.base_fields['available_colors'].widget = forms.CheckboxSelectMultiple(
            choices=Product.COLOR_PALETTE,  # Set the available color options / Встановлюємо доступні варіанти кольорів
            attrs={'class': 'form-control'}  # Add CSS class for styling / Додаємо CSS-клас для стилізації
        )
        
        # Return the customized form / Повертаємо кастомізовану форму
        return form


```


_Here's how this code is used to customize the admin panel./Ось як цей код використовується для налаштування адміністративної панелі._

* >Here, the admin.register decorator is used to register the Product model and associate it with the custom ProductAdmin class, which inherits from admin.ModelAdmin. This approach allows customization of how the Product model is displayed and edited in the Django admin interface.

* >Тут використовується декоратор admin.register для реєстрації моделі Product і пов'язання її з кастомним класом ProductAdmin, який успадковує admin.ModelAdmin. Цей підхід дозволяє налаштовувати спосіб відображення та редагування моделі Product в адміністративному інтерфейсі Django.



---

# CART APP

### CART.PY

```python

class Cart:
    def __init__(self, request):
        # Ініціалізація корзини на основі сесії користувача
        self.session = request.session
        # Отримання існуючої корзини з сесії або створення нової, якщо вона не існує
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
        
    def __iter__(self):
        product_ids = self.cart.keys()
        # Отримання всіх товарів з бази даних, що відповідають ідентифікаторам у корзині
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            # Додавання інформації про товар у корзині 
            self.cart[str(product.id)]['product'] = product
            
        for item in self.cart.values():
            # Перетворення ціни товару в десяткове число та обчислення загальної вартості
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        return len(self.cart.keys())
        
    def contains_deep(self, product_id, **params):
        # Перевіряє, чи містить корзина товар із зазначеними параметрами глибоко
        if params:
            for key, value in params.items():
                if self.cart[product_id][key] != value:
                    return False
        return True
        
    def __contains__(self, product_id, **params):
        # Перевіряє, чи містить корзина товар із зазначеним ідентифікатором
        return str(product_id) in self.cart
        
    def add(self, **data) -> dict | None:
        # Додає товар до корзини
        product_id = data.pop('product_id')
        if product_id not in self.cart:
            self.save()
            self.cart[product_id] = data
            result_data = self.cart[product_id]
            result_data['product_id'] = product_id
            return result_data
    
    def save(self):
        # Зберігає зміни в корзині у сесії
        self.session.modified = True
    
    def remove(self, product_id):
        # Видаляє товар із корзини
        del self.cart[product_id]
        self.save()
        return None
    
    def update(self, **data): 
        # Оновлює інформацію про товар у корзині
        product_id = data.pop('product_id')
        if product_id in self.cart:
            self.cart[product_id].update(**data)
            self.save()
            return self.cart[product_id]
        
    def clear(self):
        # Очищає корзину користувача
        del self.session[settings.CART_SESSION_KEY]
        self.save()


```

* >Цей код представляє клас Cart. Основне призначення класу - зберігання, оновлення та управління товарами, доданими користувачем до кошика, із збереженням стану кошика у сесії користувача. Це дозволяє користувачеві додавати, видаляти та оновлювати товари в кошику, а також зберігати зміни між запитами.

* >This code represents the Cart class, which manages the shopping cart in a Django-based web application. The main purpose of the class is to store, update and manage the products added by the user to the cart, while saving the state of the cart in the user's session. It allows the user to add, remove, and update items in the cart, as well as save changes between requests.


### FORMS.PY


```python


class CartBaseForm(forms.Form):
    # Базовий клас форми для роботи з корзиною.

    def process_request(self, request):
        # Метод для обробки запиту. Встановлює атрибут request.
        print("CALLING METHOD", request)
        self.request = request

    def save(self):
        # Метод збереження. Перевіряє валідність форми та наявність запиту.
        assert self.is_valid(), 'Form is not valid'
        assert self.request, 'Request is not provided'

class CartAddForm(CartBaseForm):
    # Форма для додавання продукту до корзини.

    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    size = forms.CharField(validators=[ProductSizeValidator(Product.ACCEPTABLE_SIZES).validate_size])
    color = forms.CharField()
    price = forms.DecimalField()
    
    def clean(self):
        # Метод очищення даних форми перевіряє, що продукт ще не доданий до корзини.
        if getattr(self, 'request', None):
            cart = Cart(self.request)
            if self.cleaned_data['product_id'] in cart:
                raise forms.ValidationError('Продукт вже знаходиться в корзині')
        return self.cleaned_data

    def save(self):
        # Перевизначений метод збереження. Викликає базовий метод збереження і додає продукт до корзини.
        super().save()
        self.cleaned_data['price'] = str(self.cleaned_data['price'])
        cart = Cart(self.request)
        return cart.add(**self.cleaned_data)
            

class CartUpdateForm(CartAddForm):
    # Форма для оновлення кількості продукту в корзині.

    def __init__(self, *args, **kwargs):
        # Конструктор класу. Змінює поведінку полів форми.
        super().__init__(*args, **kwargs)
        del self.fields['final_price']  # Видаляє поле final_price з форми
        for field in self.fields.values():
            field.required = False  # Встановлює всі поля форми як необов'язкові
        self.fields['product_id'].required = True  # Встановлює поле product_id як обов'язкове
        
    def save(self):
        # Перевизначений метод збереження. Оновлює кількість продукту в корзині.
        cart = Cart(self.request)
        return cart.update(**self.cleaned_data)
        
        
class CartRemoveForm(CartBaseForm):
    # Форма для видалення продукту з корзини.

    product_id = forms.CharField(widget=forms.HiddenInput)
    
    def clean(self):
        # Метод очищення даних форми. Перевіряє, що продукт присутній у корзині.
        if getattr(self, 'request', None):
            cart = Cart(self.request)
            if self.cleaned_data['product_id'] not in cart:
                raise forms.ValidationError('Цього продукту немає у вашій корзині')
        return self.cleaned_data

    def save(self):
        # Перевизначений метод збереження. Видаляє продукт з корзини.
        cart = Cart(self.request)
        return cart.remove(**self.cleaned_data)


```

* >Цей клас і його підкласи використовуються для управління формами, пов'язаними з корзиною покупок у веб-додатку на основі Django.
CartBaseForm є базовим класом, що забезпечує обробку запиту і збереження даних форми.
CartAddForm використовується для додавання продукту до корзини. Вона перевіряє, чи вже доданий продукт, і, якщо ні, додає його.
CartUpdateForm використовується для оновлення інформації про продукт у корзині, наприклад, кількість.
CartRemoveForm використовується для видалення продукту з корзини, перевіряючи, чи продукт дійсно присутній у корзині перед видаленням.
Ці форми спрощують процес взаємодії з корзиною покупок, забезпечуючи перевірку даних і відповідні операції з продуктами в корзині.


### VIEWS.PY

```python


class CartMixin(FormMixin, generic.View):
    
    # Міксин для роботи з кошиком, що реалізує додавання, оновлення та видалення товарів.
    
    status_code = 200  # Код стану HTTP відповіді за замовчуванням
    msg = None  # Повідомлення, яке буде надіслано у відповіді

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        # Обробник POST запиту для додавання, оновлення або видалення товару з кошика.
      
        form = self.get_form()  # Отримуємо екземпляр форми
        form.process_request(request)  # Обробляємо запит формою
        if form.is_valid():  # Перевіряємо валідність даних форми
            return self.form_valid(form)  # Якщо дані форми валідні, викликаємо метод form_valid
        else:
            return self.form_invalid(form)  # Якщо дані форми невалідні, викликаємо метод form_invalid

    def form_valid(self, form: Any) -> HttpResponse:
       
        # Метод викликається при успішній валідації форми.
       
        saved_data = form.save() or {}  # Зберігаємо дані з форми, якщо форма підтримує метод save
        return JsonResponse({'data': saved_data, 'msg': self.msg}, status=self.status_code)  # Повертаємо JSON відповідь з даними та повідомленням

    def form_invalid(self, form: Any) -> HttpResponse:
       
       # Метод викликається при помилці валідації форми.
      
        return JsonResponse({'msg': 'Помилка валідації', 'errors': form.errors}, status=422)  # Повертаємо JSON відповідь з повідомленням про помилку валідації та помилками форми

class CartAddView(CartMixin):

    # Представлення для додавання товару до кошика.
    
    form_class = forms.CartAddForm  # Вказуємо клас форми для додавання товару
    msg = 'Товар додано до кошика'  # Повідомлення про успішне додавання товару
    def form_valid(self, form: forms.CartAddForm) -> HttpResponse:
        saved_data = form.save() or {}  # Зберігаємо дані з форми, якщо форма підтримує метод save
        product_id = saved_data.get('product_id')  # Отримуємо ідентифікатор продукту з збережених даних
        serialized_product = serialize("json", [Product.objects.get(id=product_id)])  # Знаходимо продукт за ідентифікатором
        return JsonResponse({'data': {'product': serialized_product, 'cart_item': saved_data}, 'msg': self.msg}, status=self.status_code)  # Повертаємо JSON відповідь з даними та повідомленням


class CartUpdateView(CartMixin):
    
    # Представлення для оновлення кількості товару в кошику.
   
    form_class = forms.CartUpdateForm  # Вказуємо клас форми для оновлення кількості товару
    msg = 'Кількість змінено'  # Повідомлення про успішне оновлення кількості товару

class CartRemoveView(CartMixin):
   
    # Представлення для видалення товару з кошика.
    
    form_class = forms.CartRemoveForm  # Вказуємо клас форми для видалення товару
    status_code = 204  # Код стану HTTP відповіді для успішного видалення товару


```


* >Цей код реалізує представлення для управління кошиком покупок у веб-додатку на Django. Представлення забезпечують функціональність додавання, оновлення та видалення товарів з кошика через форми та відповідають на запити JSON відповідями.
CartMixin - базовий міксин, що обробляє POST запити, перевіряє валідність форми та повертає відповідні JSON відповіді.
CartAddView - представлення для додавання товару до кошика, що використовує форму CartAddForm і повертає повідомлення про успішне додавання товару.
CartUpdateView - представлення для оновлення кількості товару в кошику, що використовує форму CartUpdateForm і повертає повідомлення про успішне оновлення кількості товару.
CartRemoveView - представлення для видалення товару з кошика, що використовує форму CartRemoveForm і повертає код стану 204 при успішному видаленні товару.
Ці представлення спрощують роботу з кошиком покупок, забезпечуючи інтерактивне та асинхронне управління товарами для користувачів веб-додатку.



---

# MAIN APP

### VIEWS.PY

```python

def main_view(request):
    """
    Відображення головної сторінки з колекціями та продуктами зі знижкою більше 30%.
    Продукти групуються в групи по 4 для відображення в каруселі 
    (повертається список ітераторів по 4 елементи в кожному).
    """
    discounted_products = Product.objects.filter(discount__gte=30)
    context = {
        "collections": Collection.objects.all(),
        "discounted_products_grouped": zip_longest(
            *[iter(discounted_products)] * 4, fillvalue=None
        ),
    }
    return render(request, "main/index.html", context)

# Отримання облікових даних з Algolia
def get_algolia_credentials(request):
    # повертаємо дані для Algolia у форматі JSON
    return JsonResponse({
        # Інформацію отримуємо з файлу .env 
        "APP_ID": os.getenv("ALGOLIA_APP_ID"),
        "API_KEY": os.getenv("ALGOLIA_API_KEY")
    })

```


* >Цей код реалізує уявлення для веб-додатку на Django: функція main_view відображає головну сторінку з колекціями та продуктами зі знижкою більше 30%, групуючи їх для показу в каруселі, а функція get_algolia_credentials повертає облікові дані для Algolia у форматі JSON. env.



### MIXINS.PY


```python


class SaveSlugMixin:
    # Міксин для автоматичного збереження slug при збереженні об'єкта моделі.
    def save(self, slug_field="slug", slugify_value=None, *args, **kwargs):
        # Перевизначений метод save для збереження об'єкта моделі з генерацією та збереженням унікального slug.
        if slug_field and slugify_value:
            slug = getattr(self, slug_field)
            if not slug:
                new_slug = slugify(slugify_value)
                setattr(self, slug_field, new_slug)
                while self.__class__.objects.filter(
                    **{slug_field + "__iexact": new_slug}
                ).exists():
                    new_slug += str(
                        random.randint(0, (self.__class__.objects.count() + 1) * 100)
                    )
                    setattr(self, slug_field, new_slug)
        return super().save(*args, **kwargs)


```

* >Цей код визначає міксин SaveSlugMixin для моделей Django, який автоматично генерує і зберігає унікальний slug для об'єкта моделі при його збереженні. Міксин використовує функцію slugify для перетворення текстового значення slug, а потім перевіряє, чи існує вже такий slug в базі даних. Якщо slug не є унікальним, міксин додає до нього випадкове число і перевіряє знову, доки не буде знайдено унікальний slug.


---

# APP YOUR DESIGN

### VIEWS.PY

```PYTHON

def design_page(request):
    return render(request, 'your_design/design.html')

```

* >Це функція відображення сторінки your_design


---

# APP PAYMENTS

### VIEWS.PY

```python



def email_form(request):
    api_url = 'https://api.novaposhta.ua/v2.0/json/'
    api_key = 'my api key'

    # Отримання списку міст
    cities_response = requests.post(api_url, json={
        'apiKey': api_key,
        'modelName': 'Address',
        'calledMethod': 'getCities',
        'methodProperties': {}
    })
    cities_data = cities_response.json()['data']

    if request.method == 'POST':
        form = forms.PaymentForm(request.POST)  # Створюємо форму PaymentForm з POST-запиту
        if form.is_valid():  # Перевіряємо дійсність форми
            cd = form.cleaned_data  # Отримуємо очищені дані з форми
            cart = Cart(request)  # Створюємо об'єкт корзини
            context = {'person_data': cd, 'cart': cart, 'user': request.user}  # Формуємо контекст для шаблону

            # Генеруємо HTML-контент на основі шаблону 'payments/order_info.html' та контексту
            html_content = render_to_string('payments/order_info.html', context)
            plain_message = strip_tags(html_content)  # Створюємо звичайне текстове повідомлення без HTML-тегів
            
            # Виводимо вміст html_content та plain_message в консоль для відладки
            print(html_content, plain_message, sep="\n")

            # Надсилаємо лист
            send_mail(
                'YOUR ORDER',  # Назва повідомлення
                plain_message,  # Текст повідомлення без HTML
                settings.EMAIL_HOST_USER,  # Хто буде відправляти
                [cd["email"]],  # Одержувач повідомлення
                fail_silently=False,  
                html_message=html_content  # HTML вміст листа
            )
    elif request.method == 'GET' and 'city_id' in request.GET:
        # Обробка AJAX-запиту для отримання відділень пошти по обраному місту
        city_id = request.GET['city_id']
        post_offices_response = requests.post(api_url, json={
            'apiKey': api_key,
            'modelName': 'AddressGeneral',
            'calledMethod': 'getWarehouses',
            'methodProperties': {'CityRef': city_id}
        })
        post_offices_data = post_offices_response.json()['data']
        return JsonResponse({'post_offices': post_offices_data})
    
    # Отримання відділень пошти для першого міста
    first_city_id = cities_data[0]['Ref']
    post_offices_data = []

    if first_city_id:
        post_offices_response = requests.post(api_url, json={
            'apiKey': api_key,
            'modelName': 'AddressGeneral',
            'calledMethod': 'getWarehouses',
            'methodProperties': {'CityRef': first_city_id}
        })
        post_offices_data = post_offices_response.json()['data']

    form = forms.PaymentForm()  # Якщо метод запиту GET, створюємо порожню форму PaymentForm
    return render(request, 'payments/email_form.html', {'form': form, 'cities': cities_data,
            'post_offices': post_offices_data})  # Виводимо форму на сторінку email_form.html



```

* >Отримання списку міст: При кожному запиті до цього подання виконується запит до API "Нова Пошта" для отримання списку міст.


* >Обробка запиту POST: Якщо запит є POST, перевіряється валідність форми. Якщо форма дійсна, генерується HTML-повідомлення, яке надсилається на вказаний у формі email.


* >Обробка AJAX-запиту: Якщо запит є GET і містить параметр city_id, виконується запит до API "Нова Пошта" для отримання відділень пошти у вказаному місті та повертається JSON-відповідь з даними відділень.

* >Відображення форми та даних: Якщо запит є GET, створюється порожня форма та відображається разом зі списком міст та відділень пошти для першого міста.



### FORMS.PY 


```PYTHON


class PaymentForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефону')  # поле для введення номера телефону
    email = forms.EmailField(label='Email')  # поле для введення email
    name = forms.CharField(label='Ім`я')  # поле для введення імені
    country = CountryField().formfield(label="Країна")  # поле для вибору країни, використовуючи бібліотеку django-countries
    post = forms.CharField(label='Поштовий індекс')  # поле для введення поштового індексу
    
    # конструктор класу PaymentForm
    def __init__(self, *args, **kwargs):
        # Викликає конструктор батьківського класу (forms.Form).
        super().__init__(*args, **kwargs)
        # проходиться по всіх полях форми
        for field in self.fields:
            # Оновлює атрибути віджета кожного поля форми
            self.fields[field].widget.attrs.update({'class': 'border border-light text-white bg-black'})


```

* > Ця форма включає поля для введення номера телефону, email, імені, вибору країни та введення поштового індексу. Конструктор форми оновлює атрибути віджету кожного поля, додаючи класи CSS для стилізації.



---



# CONTACTS 

1. Danil
    * email - danilgubarev9804@gmail.com

2. Oleksii
    * email - alexxey2707@gmail.com

3. Olha
    * email - bachyrinaolya94@gmail.com

4. Vitalii
    * email - fedenkovitalya3010@gmail.com
=======
* Here, the admin.register decorator is used to register the Product model and associate it with the custom ProductAdmin class, which inherits from admin.ModelAdmin. This approach allows customization of how the Product model is displayed and edited in the Django admin interface.

Тут використовується декоратор admin.register для реєстрації моделі Product і пов'язання її з кастомним класом ProductAdmin, який успадковує admin.ModelAdmin. Цей підхід дозволяє налаштовувати спосіб відображення та редагування моделі Product в адміністративному інтерфейсі Django.






