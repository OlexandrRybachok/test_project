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
        # print(response)
        roten_tomatoes = response['Ratings']
        rotten_tomatoes = roten_tomatoes[0]
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
        awards = response['Awards']
        poster = response['Poster']
        metascore = response['Metascore']
        imdbrating = response['imdbRating']
        imdbvotes = response['imdbVotes']
        imdbid = response['imdbID']
        type_0 = response['Type']
        info_display = f"Title: {title}\nYear: {year_0}\nRated: {rated}\nReleased: {released}\nRuntime: {runtime} Genre: {genre} Director: {director} Writer: {writer} Actors: {actors} Plot: {plot} Language: {language} Country: {country} Awards: {awards} Metascore: {metascore} imdbRating: {imdbrating} imdbVotes: {imdbvotes} Type: {type_0}"
        # print(info_display)
        # while active:
        #     response = requests.get(f'https://www.omdbapi.com/?r=json&s={data}&page={page}&y={year}&apikey=36cd6ae').json()
        #     page += 1
        #     if response['Response'] == 'True':
        #         responses.append(response)
        #     else:
        #         break
        request.session['response'] = info_display
        request.session['poster'] = poster
        return redirect('movierating:results')
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movierating/new_request.html', context)

def results(request):
    """Відобразити отримані результати."""
    result = request.session['response']
    poster = request.session['poster']
    context = {'result': result, 'poster': poster}
    return render(request, 'movierating/results.html', context)