from flask import Flask, request
from pymongo import MongoClient
from flask import jsonify
import json
from bson import json_util
from pymongo.cursor import Cursor
from flask_pymongo import PyMongo
from functools import reduce


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
	
@app.route("/songs/avg/difficulty/", methods=['GET'])	
def get_avg_difficulty():
	all_songs = db.songs.find()
	columns = {'_id': 0, 'difficulty': 1}

	level = request.args.get('level')
	where = {}

	if level:
		where['level'] = int(level)

	_songs = list(map(lambda song: song['difficulty'], db.songs.find(where, columns)))
	total_items = len(_songs)
	total_value = reduce(lambda total, value: total + (value), _songs, 0)
	result =  round(total_value / total_items, 2)

	print("avg diff songs", _songs, result)
	return jsonify({"average difficulty": result})
	

		
	
if __name__ == "__main__":
	app.run(debug=True)


