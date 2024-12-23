import requests, json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import MovieForm

def index(request):
    """Домашня сторінка Test Project."""
    return render(request, 'movierating/index.html')

def new_request(request):
    """Відображення форми та здійснення запиту."""
    if request.method == 'POST':
        form = MovieForm(data=request.POST)
        data = form['title'].value()
        year = form['year'].value()
        responses = []
        page = 1
        active = True
        response = requests.get(f'https://www.omdbapi.com/?r=json&t={data}&page={page}&y={year}&apikey=36cd6ae').json()
        title = response['Title']
        year_0 = response['Year']
        rated = response['Rated']
        released = response['Released']
        runtime = response['Runtime']
        genre = response['Genre']
        director = response['Director']
        writer = response['Writer']
        actors = response['Actors']
        plot = response['Plot']
        language = response['Language']
        country = response['Country']
        metascore = response['Metascore']
        imdbrating = response['imdbRating']
        imdbvotes = response['imdbVotes']
        type_0 = response['Type']
        poster = response['Poster']
        request.session['title'] = title
        request.session['year_0'] = year_0
        request.session['rated'] = rated
        request.session['released'] = released
        request.session['runtime'] = runtime
        request.session['genre'] = genre
        request.session['director'] = director
        request.session['writer'] = writer
        request.session['actors'] = actors
        request.session['plot'] = plot
        request.session['language'] = language
        request.session['country'] = country
        request.session['metascore'] = metascore
        request.session['imdbrating'] = imdbrating
        request.session['imdbvotes'] = imdbvotes
        request.session['type_0'] = type_0
        request.session['poster'] = poster
        # while active:
        #     response = requests.get(f'https://www.omdbapi.com/?r=json&s={data}&page={page}&y={year}&apikey=36cd6ae').json()
        #     page += 1
        #     if response['Response'] == 'True':
        #         responses.append(response)
        #     else:
        #         break
        return redirect('movierating:results')
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movierating/new_request.html', context)

def results(request):
    """Відобразити отримані результати."""
    title = request.session['title']
    year_0 = request.session['year_0']
    rated = request.session['rated']
    released = request.session['released']
    runtime = request.session['runtime']
    genre = request.session['genre']
    director = request.session['director']
    writer = request.session['writer']
    actors = request.session['actors']
    plot = request.session['plot']
    language = request.session['language']
    country = request.session['country']
    metascore = request.session['metascore']
    imdbrating = request.session['imdbrating']
    imdbvotes = request.session['imdbvotes']
    type_0 = request.session['type_0']
    poster = request.session['poster']
    context = {
        'title': title,
        'year_0': year_0,
        'rated': rated,
        'released': released,
        'runtime': runtime,
        'genre': genre,
        'director': director,
        'writer': writer,
        'actors': actors,
        'plot': plot,
        'language': language,
        'country': country,
        'metascore': metascore,
        'imdbrating': imdbrating,
        'imdbvotes': imdbvotes,
        'type_0': type_0,
        'poster': poster,
    }
    return render(request, 'movierating/results.html', context)