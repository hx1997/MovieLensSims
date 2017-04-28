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

def simPearson(prefs, user1, user2):
	user1Mean = 0
	user2Mean = 0

	if len(prefs[user1]) * len(prefs[user2]) == 0:
		return 0

	for item in prefs[user1]:
		user1Mean += prefs[user1][item]
	user1Mean /= len(prefs[user1])

	for item in prefs[user2]:
		user2Mean += prefs[user2][item]
	user2Mean /= len(prefs[user2])

	num = 0
	deno1 = 0
	deno2 = 0
	for item in prefs[user1]:
		if item in prefs[user2]:
			print item
			num += (prefs[user1][item] - user1Mean) * (prefs[user2][item] - user2Mean)
			deno1 += pow(prefs[user1][item] - user1Mean, 2)
			deno2 += pow(prefs[user2][item] - user2Mean, 2)

	deno = math.sqrt(deno1 * deno2)

	if deno == 0: return 0

	correlation = num / deno

	return correlation

def findNearestNeighbor(prefs, user, corFunc = simPearson):
	max = 0
	maxUser = {}

	for userid in prefs:
		if userid != user:
			correlation = corFunc(prefs, userid, user)
			if correlation > max:
				max = correlation
				maxUser = userid

	return (max, maxUser)