#!/usr/bin/env python


from game_rank import *



class ExpPlayer(Player):
	def __init__(self, skill=None):
		super(ExpPlayer, self).__init__(skill=skill)
		self.exp = 0
	def gainExp(self, exp):
		self.exp = self.exp + exp
	def decayExp(self, percent):
		self.exp = self.exp * percent
	def __str__(self):
		return "ExpPlayer(skill="+str(self.skill)+", exp="+str(self.exp)+")"


rounds_in_game = 20
percent_decay = 0.95

player_pool_size = 1000
num_games = 100



player_pool = []

for _ in range(player_pool_size):
	player_pool.append(ExpPlayer())

for i in range(num_games):
	games = [ PlayerGame(player_pool[i*20:i*20+19]) for i in range(player_pool_size / 20) ]


	for i in range(rounds_in_game):
		for game in games:
			game.playRound()

	# player_pool = []

	for game in games:
		players = game.playersByScore()
		for i in range(len(players)):
			players[i].gainExp(i)
		# player_pool = player_pool + players

	for p in player_pool:
		p.decayExp(percent_decay)
		p.evolveSkill()

	player_pool = sorted(player_pool, key=lambda p: p.exp)
	# print [ str(p) for p in player_pool ]

	print measureSkillOrder(player_pool)

# print [ str(p) for p in player_pool ]

