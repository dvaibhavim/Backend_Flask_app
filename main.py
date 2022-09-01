from flask import Flask
from pymongo import MongoClient
from flask import jsonify

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.songs
songs_music = db.songs

@app.route("/")
def home():
    return "Hello, World!"
	
@app.route("/songs")
def songs():
	all_songs = songs_music.find()
	return jsonify(all_songs)
	
	
	
    
if __name__ == "__main__":
    app.run(debug=True)


