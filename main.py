from flask import Flask, request
from pymongo import MongoClient
from flask import jsonify
import json
from bson import json_util
from pymongo.cursor import Cursor
from flask_pymongo import PyMongo
from functools import reduce
import re
from bson import ObjectId


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

	return jsonify({"average difficulty": result})
	
@app.route("/songs/search/", methods=['GET'])
def search_song():

	song = request.args.get('message')
	print("message is", song)

	if not song:
		return jsonify({"error": "no song title/artist given. Kindly enter title/artist for searching song"})
	
	search_query = re.compile(song, re.IGNORECASE)
	where = {
		'$or': [
			{'title': search_query},
			{'artist': search_query},
		]
	}

	result = db.songs.find(where)
	result = [r for r in result]
	print("query result are", result)

	return jsonify({"songs are": result})

@app.route("/songs/rating/", methods = ['POST'])
def add_rating():
	data = request.json
	print("request is", data.get('song_id'), data.get('rating'), request.json)

	try:
		if not data.get('song_id'):
			return jsonify({'error':'song id must be specified'})
	except:
		pass

	song_id = ObjectId(data.get('song_id'))
	if not db.songs.find({'_id': {'$exists': True, '$in': [song_id]}}):
		return jsonify({'error':'Song not found'})

	try:
		rating = int(data.get('rating'))  # Raises value error
		if 1 > rating or rating > 5:
			raise ValueError()
	except ValueError:
		return jsonify({'error':'Invalid valid for "rating" param.'})
	except TypeError:
		return jsonify({'error':'Required "rating" not sent'})

	db.ratings.insert_one({
		'value': rating,
		'song_id': song_id,
	})

	return jsonify({'success':'rating added'})


@app.route("/songs/avg/rating/<string:song_id>", methods=['GET'])
def get_avg_rating(song_id):
	ratings_count = 0
	rating_sum = 0
	rating_max = 0
	rating_min = 0


	song = db.ratings.find({'song_id':ObjectId(song_id)})
	print("song is", song)
	for rating in song:
		# O(1)
		if rating['value']:
			print('ratings is', rating['value'])
			ratings_count += 1
			rating_sum += rating['value']
			rating_max = rating_max if rating_max > rating['value'] else rating['value']
			rating_min = rating_min if rating_min < rating['value'] else rating['value']

	average = round(rating_sum / ratings_count, 2) if ratings_count else 0

	return jsonify({'min': rating_min, 'max': rating_max, 'average': average})


if __name__ == "__main__":
	app.run(debug=True)


