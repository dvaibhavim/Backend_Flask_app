from flask import Flask
from pymongo import MongoClient
from flask import jsonify
import json
from bson import json_util
from pymongo.cursor import Cursor
from flask_pymongo import PyMongo


app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/Songs")

db = mongodb_client.db
songs_music = db.Songs

@app.route("/")
def home():
    return "Hello, World!"
	
@app.route("/songs", methods=['GET'])
def songs():
	all_songs = db.Songs.find()
	print(all_songs, flush=True)

	#result = [song for song in all_songs]
	print(json.dumps(all_songs), flush=True)
	#print(songs_music.find_one(), flush = True)
	return jsonify(message="success")
	
	
	
    
if __name__ == "__main__":
    app.run(debug=True)


