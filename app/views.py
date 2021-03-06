from django.shortcuts import render
from django.views.generic import (View, TemplateView, 
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DetailView)
from . import models


# Create your views here.


class IndexView(TemplateView):
    template_name = 'app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injection'] = 'Basic injection'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'app/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal','location')
    model = models.School
