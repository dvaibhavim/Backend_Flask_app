from flask import Flask
from pymongo import MongoClient
from flask import jsonify
import json
from bson import json_util
from pymongo.cursor import Cursor
from flask_pymongo import PyMongo


app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/songs")

db = mongodb_client.db
songs_music = db.songs

@app.route("/")
def home():
    return "Hello, World!"
	
@app.route("/songs/", methods=['GET'])
def songs():
	all_songs = db.songs.find()
	result = {}
	cnt = 0
	for i in all_songs:
		result[str(cnt)] = str(i['title'])
		cnt += 1
	return jsonify(result)
	
	
	
    
if __name__ == "__main__":
    app.run(debug=True)


