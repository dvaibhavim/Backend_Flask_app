from threading import Thread


#! /usr/bin/env python
import os
import sys
sys.path.append(os.path.realpath('..'))
from  main  import add_rating, app

Thread(target=app.run, kwargs={'port': 5123}).start()


class TestSongs:
    def test_that_it_returns_songs(self):
        client = flaskApp.test_client()
        response = client.get('/songs/')

        assert len(response.json)>0


class TestAverageDifficulty:
    def test_that_it_returns_average_difficulty(self):
        client = flaskApp.test_client()
        response = client.get('/songs/avg/difficulty/')

        assert 'average' in response.json

class TestSongsSearch:
    def Test_that_it_returns_song_by_artist_or_title(self):
        client = flaskApp.test_client()
        response = client.get('/songs/search/')
        assert 'songs' in response.json


class TestAddRating:
    client = flaskApp.test_client()
    def Test_that_it_returns_error_without_songid(self):
        response = client.post('/songs/rating/')

        assert 'error' in response.json

   


class TestAverageRating:
    def test_that_it_returns_average_min_and_max(self):
        song = songs_collection.find_one({}, {'_id': 1})
        client = flaskApp.test_client()
        response = client.get('/songs/avg/rating/{}/'.format(song['_id']))

        assert 'min' in response.json
        assert 'max' in response.json
        assert 'average' in response.json

