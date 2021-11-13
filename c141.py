import csv
from flask import Flask, json,request,jsonify

allmovies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

likedmovies = []
notlikedmovies = []
notwatched = []


app = Flask(__name__)
@app.route('/getmovie')
def getmovie():
    return jsonify({
        'data': allmovies[0],
        'status': 'success'
    })

@app.route('/likedmovie', methods = ['POST'])
def likedmovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    likedmovies.append(movie)
    return jsonify({
        'status':'success'
    }),201

@app.route('/notliked', methods = ['POST'])
def notliked():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notlikedmovies.append(movie)
    return jsonify({
        'status':'success'
    }),201

@app.route('/didntwatch', methods = ['POST'])
def didntwatch():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notwatched.append(movie)
    return jsonify({
        'status':'success'
    })

if __name__ == '__main__':
    app.run()