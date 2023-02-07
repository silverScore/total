from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db import models
from .models import Care
# from .models import Review
from .models import Address
from django.db.models import Q

# Create your views here.

# generic
# listView
class CareListView(ListView):
    model = Care