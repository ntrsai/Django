from django.shortcuts import render
from django.http import HttpResponse
from movie.models import movie


# Create your views here.
def getallmovies(request):
    all_movies=movie.objects.all()
    print(all_movies)
    for movies in all_movies:
        print(movie.id,movie.name,movie.release_date)
    #return HttpResponse("hello")
   
    data={}
    data['movies']=all_movies
    return render(request,'movie/index.html',context=data)
    
