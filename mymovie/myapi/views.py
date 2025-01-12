from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    allMovies = Movie.objects.all() #select * from Movies
    
    context = {
        'Movie': allMovies,
    }

    return render(request, 'myapi/index.html', context)
    
#details page
def detail(request, id):
    movie = get_object_or_404(Movie, id=id) #select * from Movies where id = id
    
    context = {
        'movie': movie,
    }

    return render(request, 'myapi/details.html', context)

#adding a movie
def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = MovieForm(request.POST or None)
                 #check if the form is valid
                if form.is_valid():
                    data=form.save(commit= False)
                    data.save()
                    return redirect('myapi:home')
            else:
                form = MovieForm()
            return render(request, 'myapi/addmovies.html', {'form': form})
        else:
            return redirect('myapi:home')
    return redirect('accounts:login')

#editing movies
def edit_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
             #get the movie with the respective id
             movie = Movie.objects.get(id=id)
             #check if the request is a POST request
             if request.method == 'POST':
                form = MovieForm(request.POST or None, instance=movie)
                 #check if the form is valid
                if form.is_valid():
                    data=form.save(commit= False)
                    data.save()
                    return redirect('myapi:detail', id)
             else:
                form = MovieForm(instance=movie)
             return render(request, 'myapi/addmovies.html', {'form': form})
        else:
             return redirect('myapi:home')
    return redirect('accounts:login')
def delete_movies(request, id):
    if request.user.is_authenticated:
         if request.user.is_superuser:
             movie = Movie.objects.get(id=id)
             movie.delete()
             return redirect('myapi:home')
         else:
             return redirect('myapi:home')
    return redirect('accounts:login')


def add_review(request, id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=id)
        
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                # Save the review without committing to the database yet
                review = form.save(commit=False)
                review.user = request.user  # Set the user to the current logged-in user
                review.movie = movie  # Set the movie for this review
                review.save()  # Save the review to the database
                return redirect('myapi:detail', id=id)  # Redirect to the movie detail page
        else:
            form = ReviewForm()  # Initialize the form if the request method is not POST
        
        return render(request, 'myapi/details.html', {'form': form, 'movie': movie})

    return redirect('accounts:login')  # Redirect to login if user is not authenticated
