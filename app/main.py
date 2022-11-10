from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from tmdbv3api import TMDb
from tmdbv3api import Movie

import random

app = Flask(__name__)
CORS(app)

# tmdb setup
tmdb = TMDb()
tmdb.api_key = 'e70f4a66202d9b5df3586802586bc7d2'
tmdb.language = 'en'
tmdb.debug = True
movie = Movie()
  
@app.route("/", methods=['POST'])
@cross_origin
def recommendation():
    movies = request.get_json()
    print(movies)

    movieIDs, recommendedMovies = [], []
    for m in movies:
        search = movie.search(m)
        for res in search:
            movieIDs.append(res.id)
    for id in movieIDs:
        recos = movie.recommendations(id)
        for reco in recos:
            recommendedMovies.append(reco.title)
    sampledRecos = random.sample(recommendedMovies, 5)
    response = jsonify(sampledRecos)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response