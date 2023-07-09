# Edit web/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Book
from django.urls import reverse_lazy


class Index(LoginRequiredMixin,TemplateView):
    template_name = "web/purple.html"
    
    
class Form(TemplateView):
    template_name = "web/pages/forms/basic_elements.html"
    
    
class Icon(TemplateView):
    template_name = "web/pages/icons/mdi.html"
    
    
class Button(TemplateView):
    template_name = "web/pages/ui-features/buttons.html"
    
    
class Typography(TemplateView):
    template_name = "web/pages/ui-features/typography.html"
    
    
class Chart(TemplateView):
    template_name = "web/pages/charts/chartjs.html"
    
    
class Table(TemplateView):
    template_name = "web/pages/tables/basic-table.html"
    
    
class Error(TemplateView):
    template_name = "pages/error-404.html"


class BookCreate(LoginRequiredMixin , CreateView):
    model = Book
    fields = '__all__'
    template_name = 'web/book_form.html'
    # success_url = reverse_lazy('app:booklist')

    def get_success_url(self):
        return reverse_lazy('app:bookdetail', kwargs={'pk': self.pk})


class BookList(LoginRequiredMixin , ListView):
    model = Book
    template_name = 'web/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'booklist'
        return context

    
class BookDetail(LoginRequiredMixin , DetailView):
    model =  Book
    template_name = "web/book_detail.html"
    fields = '__all__'

class BookUpdate(LoginRequiredMixin , UpdateView):
    model =  Book
    template_name = "web/book_update.html"
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy('app:booklist')


class BookDelete(LoginRequiredMixin , DeleteView):
    model =  Book
    template_name = "web/book_delete.html"
    fields = '_all_'

    def get_success_url(self):
        return reverse_lazy('app:booklist')