#!/usr/bin/env python



import random




class Player(object):
	def __init__(self, skill=None):
		if skill is None:
			self.skill = random.randint(0, 100)
		else:
			self.skill = skill # between 0 and 100
	def evolveSkill(self, amount=3):
		self.skill = self.skill + random.randint(-amount, amount)
		if self.skill < 0:
			self.skill = 0
		elif self.skill > 100:
			self.skill = 100
	def attemptScore(self):
		return self.skill >= random.randint(1, 100)
	def __str__(self):
		return "player(skill="+str(self.skill)+")"




class PlayerGame(object):
	def __init__(self, players=[]):
		self.players = [ [p, 0] for p in players ]
	def addPlayer(self, player):
		self.players.append([player, 0])
	def playRound(self):
		for ps in self.players:
			if ps[0].attemptScore():
				ps[1] = ps[1] + random.randint(1, 3)
	def playersByScore(self):
		return [ ps[0] for ps in sorted(self.players, key=lambda ps: ps[1]) ]
	def __str__(self):
		return "playerGame(" + str([ str(ps[0])+":"+str(ps[1]) for ps in self.players ]) +")"




def measureSkillOrder(players):
	ranks = list(range(len(players)))
	ranks = sorted(ranks, key=lambda i: players[i].skill)

	error = 0
	# print ranks
	for i in range(len(ranks)):
		error = error + abs((ranks[i] - i) / float(len(ranks)))

	return error




# game = playerGame([ player() for _ in range(5) ])

# for _ in range(5):
# 	game.playRound()

# print game
# print [ str(p) for p in game.playersByScore() ]

