from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView, FormView, DetailView

from market.forms import ProductForm, AuthorRegistrationForm, AuthorLoginForm
from market.models import Author, Product


# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"


class AuthorCreateView(CreateView):
    model = Author


class ProductListView(TemplateView):
    template_name = "market/explore.html"


class ProductCreateView(CreateView):
    model = Product
    template_name = "market/create.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('product-list')


class ProductDetailView(TemplateView):
    template_name = "market/details.html"


class ProductUpdateView(ListView):
    pass


class ProductDeleteView(ListView):
    pass


class AuthorListView(ListView):

    pass


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'market/author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(author=self.object)
        return context


class SignUpView(FormView):
    form_class = AuthorRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "User successfully registered")
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})


class SignInView(View):
    def get(self, request):
        form = AuthorLoginForm
        return render(request, "signin.html", context={"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You have logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            return render(request, "sigin.html", {"form": form})


class ProfileView(View):
    pass


