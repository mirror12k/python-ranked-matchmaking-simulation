#!/usr/bin/env python



import random




class Player(object):
	def __init__(self, skill=None):
		if skill is None:
			self.skill = random.randint(0, 100)
		else:
			self.skill = skill # between 0 and 100
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
				ps[1] = ps[1] + 1
	def playersByScore(self):
		return [ ps[0] for ps in sorted(self.players, key=lambda ps: ps[1]) ]
	def __str__(self):
		return "playerGame(" + str([ str(ps[0])+":"+str(ps[1]) for ps in self.players ]) +")"





# game = playerGame([ player() for _ in range(5) ])

# for _ in range(5):
# 	game.playRound()

# print game
# print [ str(p) for p in game.playersByScore() ]

