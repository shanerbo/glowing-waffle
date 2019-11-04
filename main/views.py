from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import New, NewCategory, NewSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import NewUserForm


# Create your views here.
def single_slug(request, single_slug):
    categories = [c.category_slug for c in NewCategory.objects.all()]
    if single_slug in categories:
        matching_series = NewSeries.objects.filter(new_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = New.objects.filter(new_series__new_series=m.new_series).values('new_slug').earliest(
                'new_publish')
            series_urls[m] = part_one['new_slug']

        return render(request,
                      template_name="main/category.html",
                      context={"part_ones": series_urls},
                      )

    news = [c.new_slug for c in New.objects.all()]
    if single_slug in news:
        this_new = New.objects.get(new_slug=single_slug)
        news_from_series = New.objects.filter(new_series__new_series=this_new.new_series).order_by('new_publish')
        this_new_idx = list(news_from_series).index(this_new)
        print(this_new.new_series)
        return render(request,
                      template_name="main/new.html",
                      context={"new": this_new, "sidebar": news_from_series, "this_new_idx": this_new_idx})

    return HttpResponse(f"{single_slug} does not correspond to anything.")


def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": NewCategory.objects.all},
                  )


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form},
                  )


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("main:homepage")


def login_request(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, f"You are logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    return render(request,
                  "main/login.html",
                  {"form": form},
                  )
