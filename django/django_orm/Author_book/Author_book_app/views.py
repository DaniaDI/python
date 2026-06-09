from django.shortcuts import render,redirect
from .models import Book ,Author
# Create your views here.


def add_book(request):
    if request.method == 'POST':
        title=request.POST['title']
        desc=request.POST['desc']
        Book.objects.create(title=title,desc=desc)
        return redirect('/')
    context= {
          'all_books' : Book.objects.all()
        }
       
    return render(request, "book.html", context)


def view_book(request, id):
    # 1. Fetch the specific book using the ID from the URL
    this_book = Book.objects.get(id=id)
    
    # 2. Handle the POST request when the user submits the form to add an author
    if request.method == 'POST':
        author_id = request.POST['author_id']
        this_author = Author.objects.get(id=author_id)
        
        # Add this author to this book's many-to-many relationship
        # (Using 'books' because that is your model's related_name)
        this_book.authors.add(this_author)
        
        # Always redirect after a successful POST request to prevent duplicate submissions
        return redirect(f'/books/{id}') 
    
    # 3. Handle to the view file
    context = {
        'book': this_book,
        # Get all authors already linked to this book
        'book_authors': this_book.authors.all(),
        # Get all authors who aren't linked to this book yet (for the dropdown list)
        'other_authors': Author.objects.exclude(book_author=this_book)
    }
    
    return render(request, "book_show.html", context)


def add_author(request):
    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        notes =request.POST['notes']
        author=Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)
        return redirect('/add_author/')
    context={
        "all_authors":Author.objects.all()
        }
    return render(request,'author.html',context)

def view_author(request,id):
    this_author = Author.objects.get(id=id)

    if request.method == 'POST':
        book_id=request.POST['book_id']
        this_book = Book.objects.get(id=book_id)
        this_author.book_author.add(this_book)
        return redirect(f'/authors/{id}')
    context={
        'author':this_author,
        'book_authors':this_author.book_author.all(),
        'other_books':Book.objects.exclude(authors=this_author)


    }
    return render(request, "author_show.html", context)



