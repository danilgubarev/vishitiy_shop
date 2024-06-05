from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView as DjangoLogoutView, LoginView as DjangoLoginView
from django.contrib import messages

User = get_user_model()

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    if request.method == "POST": 
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, "Аккаунт був успішно створений")
           return redirect("users:login")
    return render(request, "registration/signup.html", {"form": form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, f"Ви увійшли як {user.username}")
    return render(request, "registration/login.html", {"form": form})

       
class LogoutView(DjangoLogoutView):
    http_method_names = ["post", "options", "get"]
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("users:login")
        return render(self.request, "registration/logout.html")
    
class LoginView(DjangoLoginView):
    def form_valid(self, form):
        print("You should see messages here")
        messages.success(self.request, "Ви увійшли як {}".format(form.get_user().username))
        return super().form_valid(form)
    