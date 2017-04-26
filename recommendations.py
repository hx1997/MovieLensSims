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

def simDistance(prefs, user1, user2):
	distance = 0
	for item in prefs[user1]:
		if item in prefs[user2]:
			distance += pow(prefs[user1][item] - prefs[user2][item], 2)

	if distance == 0: return 0

	correlation = 1 / (1 + math.sqrt(distance))

	return correlation

def findNearestNeighbor(prefs, user, corFunc = simDistance):
	max = 0
	maxUser = {}

	for userid in prefs:
		if prefs[userid] != user:
			correlation = corFunc(prefs, userid, user)
			if correlation > max:
				max = correlation
				maxUser = userid

	return (max, maxUser)