from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from . import models



#search
def searchView(request):
    query = request.GET.get('s', '')
    book = models.Book.objects.filter(title__icontains=query) if query else models.Book.none
    context = {
        'book': book,
        's': query
    }
    return render(request, template_name='books/book.html', context=context)

#detailView

def bookDetailView(request, id):
    book = get_object_or_404(models.Book, id=id)
    average_rating = models.Review.objects.filter(book=book).aggregate(Avg('rating'))['rating__avg']

    context = {
        'book': book,
        'average_rating': round(average_rating, 1) if average_rating else 'Нет оценок'
    }

    return render(request, 'books/book_detail.html', context)

#listView
def bookListView(request):
    if request.method == 'GET':
        book = models.Book.objects.all()
        context = {
            'book': book
        }
    return render(request, template_name='books/book.html', context=context)