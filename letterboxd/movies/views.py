from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})

#

    
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return redirect('home')
    

from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Debug print statement for form errors
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        return response

    def get_success_url(self):
        return reverse_lazy('login')
    

#EL LOGIN YA FUNCIONA, NO TOCAR
class OptionalLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Nombre o Contraseña icorrectos")
        return super().form_invalid(form)