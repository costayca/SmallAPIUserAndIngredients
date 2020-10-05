from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "name": "Avengers: Endgame",
        "cast": ["Chris Evans", "Robert Downey Jr.", "Mark Ruffalo"],
        "genres": ["Action", "Adventure", "Drama" , "Sci-Fi"]
    },
    {
       "name": "The Godfather ",
       "cast": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

@app.route('/movies', methods=['GET'])
def hello():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200

app.run()