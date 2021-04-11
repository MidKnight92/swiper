from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from django.urls import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import requests
import json
import itertools
from sqlalchemy.sql import expression # to be removed 
from my_app.price import get_current_price, assess_price
from my_app.contact import send_email
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .forms import LoginForm, SignupForm

User = get_user_model()

# Change to an empty list
# have users sign up to find prices at there favorite stores
# send an text when item reaches desired price range
def track(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # # Pass in the 
    # driver.get(url)
    # time.sleep(2)

# Views
def index_view(request):
    return render(request, 'my_app/index.html')

def signup_view(request):
    message = ''
    # User made a post request via creating an account
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            extra_fields = {"phone_number" : phone_number}
            user = User.objects.create_user(username=username, email=email,  password=password)
            print('sign up successful')
            login(request, user)
            # return redirect('index_view')
        else:
            message = 'Invalid Sign Up'
    form = SignupForm()
    context = {'form': form, 'message': message}
    # User made a GET request or invalid POST render signup form 
    return render(request, "my_app/registration/signup.html", context)

def login_view(request):
    message = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            print('log in successful')
            return redirect("/")
        else:
            print('log in failed')
            message = "Log In Failed"
    form = LoginForm()
    context = {'form': form, 'message': message}
    return render(request, "my_app/registration/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

# TODO add login required declaration
@csrf_exempt
def search_view(request):
    # User made a GET request scraping results for particular item via Walmart.com
    if request.method == "GET":

        # Get headers
        header = {
            'User-Agent': request.headers['User-Agent'],
            'referer': request.headers['referer']
        }
    
        # Get user input
        item_searched = request.GET["item"]
       
        # Add item searched into model
        ## models.Search.objects.create(search=item)

        # urlify user input
        urlify_item_searched = quote_plus(item_searched)

        URL = f'https://www.walmart.com/search/?query={urlify_item_searched}'
        response = requests.get(URL, headers=header)
        data = response.text
     
        # Create parsed data
        soup = BeautifulSoup(data, 'html.parser')
        # print(soup)

        # images
        item_image_urls = soup.select('#searchProductResult img')
        
        item_image_urls = [img['src'] for img in item_image_urls]
        item_image_urls = [img.split('?')[0] for img in item_image_urls]


        # prices
        item_price_spans = soup.find_all('span', {'class': 'price-main-block'})
        item_price_spans = [span.find_all('span',{'class': 'visuallyhidden'}) for span in item_price_spans]
        item_prices = [span[0].text for span in item_price_spans]
        
        # titles
        item_title_divs = soup.find_all('div', {'class': 'search-result-product-title'})
        item_titles = [div.get_text() for div in item_title_divs]
        item_titles = [text.replace('Product Title', '') for text in item_titles]

        # Create a collection of item title, price, and image information
        list_of_item_tuples = []
        for (title, price, image) in itertools.zip_longest(item_titles, item_prices, item_image_urls, fillvalue=None):
            list_of_item_tuples.append((title, price, image))
        
        return render(request, 'my_app/search.html', {
            "item_searched": item_searched,
            "items": list_of_item_tuples
        })
    # TODO
    # User made a post request by adding an item to their watch list
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)       
            price_str = get_current_price(data)
            
            return HttpResponse('GOOD') #to be removed
            # return HttpResponse(status=201)
        except expression as identifier:
            print('error')
            # return HttpResponse(status=418)
            return HttpResponse("ERROR") #to be removed
    # TODO
    # User made a put request by removig an item from their watch list
    else:
        try:
            data = json.loads(request.body)
            return HttpResponse('GOOD')
        except expression as identifier:
            return HttpResponse('BAD')
        