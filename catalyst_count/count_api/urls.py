from django.urls import path
from .views import *

urlpatterns = [
    path('filter/', FilterCountView.as_view(), name = 'filter')
]

# to test it on post man
# localhost:8000/filter/?name=enter_name&industry=enter_industry...