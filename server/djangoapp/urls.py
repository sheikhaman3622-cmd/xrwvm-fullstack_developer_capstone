from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views  # make sure views.py has get_cars function

app_name = 'djangoapp'

urlpatterns = [
    # Path to get all cars
    path('get_cars/', views.get_cars, name='getcars'),

    # You can add more paths here later
    # Example:
    # path('login/', views.login_user, name='login'),
    # path('add_review/', views.add_review, name='add_review'),
    # path('dealer_reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)