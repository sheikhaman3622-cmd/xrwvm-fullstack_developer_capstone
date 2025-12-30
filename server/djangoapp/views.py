# server/djangoapp/views.py

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
import logging

from .models import CarMake, CarModel
from .populate import initiate
#from .models import Dealership, Review  # if you have these models

# Logger
logger = logging.getLogger(__name__)

# ----------------------------
# User Authentication
# ----------------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    response = {"userName": username}
    if user is not None:
        login(request, user)
        response["status"] = "Authenticated"
    return JsonResponse(response)

# ----------------------------
# Cars Endpoint
# ----------------------------
@csrf_exempt
def get_cars(request):
    count = CarMake.objects.count()
    if count == 0:
        initiate()  # populate initial data

    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name,
            "Year": car_model.year,
            "Type": car_model.type
        })
    return JsonResponse({"CarModels": cars})

# ----------------------------
# Dealership Endpoints
# ----------------------------
@csrf_exempt
def fetch_dealers(request):
    dealers = Dealership.objects.all()
    data = list(dealers.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def fetch_dealer_by_id(request, dealer_id):
    dealer = get_object_or_404(Dealership, id=dealer_id)
    data = {
        "id": dealer.id,
        "city": dealer.city,
        "state": dealer.state,
        "address": dealer.address,
        "zip": dealer.zip,
        "lat": dealer.lat,
        "long": dealer.long,
        "short_name": dealer.short_name,
        "full_name": dealer.full_name
    }
    return JsonResponse(data)

@csrf_exempt
def fetch_dealers_by_state(request, state):
    dealers = Dealership.objects.filter(state=state)
    data = list(dealers.values())
    return JsonResponse(data, safe=False)

# ----------------------------
# Reviews Endpoints
# ----------------------------
@csrf_exempt
def fetch_reviews(request):
    reviews = Review.objects.all()
    data = list(reviews.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def fetch_reviews_by_dealer(request, dealer_id):
    reviews = Review.objects.filter(dealership=dealer_id)
    data = list(reviews.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def insert_review(request):
    data = json.loads(request.body)
    review = Review.objects.create(
        name=data.get('name'),
        dealership=data.get('dealership'),
        review=data.get('review'),
        purchase=data.get('purchase', False),
        purchase_date=data.get('purchase_date', None),
        car_make=data.get('car_make', ''),
        car_model=data.get('car_model', ''),
        car_year=data.get('car_year', None)
    )
    return JsonResponse({"status": "Review added", "id": review.id})