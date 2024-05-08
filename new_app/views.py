from django.shortcuts import render
from .models import movies
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movie_list=movies.objects.all()
    
    movie_name=request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_list=movie_list.filter(name__icontains=movie_name)
    paginator=Paginator(movie_list,1)
    page = request.GET.get('page')
    movie_list = paginator.get_page(page)
    return render(request,'movie_list.html',{'movie_objects':movie_list})

    


