import math

def loadMovieLens(path='./datasets/ml-latest-small'):
	movies = {}
	for line in open(path + '/movies.csv'):
		(id, title) = line.split(',')[0:2]
		movies[id] = title

	prefs = {}
	for line in open(path + '/ratings.csv'):
		(user, movieid, rating, ts) = line.split(',')
		prefs.setdefault(user, {})
		if rating != 'rating': prefs[user][movies[movieid]] = float(rating)

	return prefs

def simsDistance(user1, user2):
	distance = 0
	for item in user1:
		if item in user2:
			distance += pow(user1[item] - user2[item], 2)

	distance = 1 / (1 + math.sqrt(distance))

	return distance

def findNearestNeighbor(user):
	pass