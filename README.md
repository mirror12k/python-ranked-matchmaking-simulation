# python-ranked-matchmaking-simulation
simulates a simple pool of players of varying skill who are placed in various games together and given the opportunity to score points based on their skill.

after a game is completed, players are awarded exp based on how high on the score board they are (from 1st to 24th),
this mimics the current tf2 casual matchmaking system in a primitive way.

to fix the problem of infinite exp growth, a constant exp decay of 5% is applied to all players after a full cycle of games, that way higher rank players have to use their skill to keep a high amount of exp and keep high up in rank,
while lower skilled players won't be able to muster enough exp to enter higher-level games due to the decay.

because exp is still preserved, it doesn't prevent a player from eventually getting to the higher games if they improve in skill.
it simply allows easy ranking and matchmaking of players of similar calibre.
