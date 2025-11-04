from django.shortcuts import render, get_object_or_404
from . import models


def bookDetailView(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        context = {
            'book_id': book_id
        }
    return render(request, template_name='books/book_detail.html', context=context)


def bookListView(request):
    if request.method == 'GET':
        book = models.Book.objects.all()
        context = {
            'book': book
        }
    return render(request, template_name='books/book.html', context=context)