from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    # context_object_name = 'anything_you_want'

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_new.html'
    fields = ['title', 'short_desc', 'desc']

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'short_desc', 'desc']
    template_name = 'books/book_edit.html'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('home')