import random
class Unit(object):
	def __init_(self):
		self.name = name
		self.energy = 5
		self.health = 100
		self.strength = 5
		self.intelligence = 5
		self.dexterity = 5
		self.defense = self.level * 1.5 + self.strength * 2
		self.evade = self.level * 1.5 + self.dexterity * 2
		self.will = self.level * 1.5 + self.intelligence * 2
		self.level = 1
		#THIS IS THE MOVEMENT/MAP STUFF?
	def move(self, choice):
		#THIS IS THE BATTLE ACTIONS/CALCUATIONS
	def attack(self):
		self.hitChance = hitChance
		self.dmgDealt = dmgDealt
		#self.scanOnChoice should be part of the LOOP 
		# self.findTargets is part of scanOnChoice, in the LOOP

	def dmg(self):
		#target unit's health -= dmgDealt

	def userInput(self):
		#convert user input into "choice"
		#prompt and take userInput

class Warrior(Unit):
	def __init_(self):
		super(Warrior, self).__init__()
		self.strength = 15
		self.dexterity = 10
		self.OptionSet = {
			Slash:{max:5,min:0,type:"physical",range:1},
			RockToss:{max:1,min:0,type:"physical",range:5}
			}

class Archer(Unit):
	def __init_(self):
		super(Archer, self).__init__()
		self.dexterity = 15
		self.strength = 7
		self.magic = 7
		self.OptionSet = {
			DaggerStab:{max:3,min:0,type:"physical",range:1},
			ShootArrow:{max:5,min:0,type:"physical",range:10}
			}

class Mage(Unit):
	def __init_(self):
		super(Mage, self).__init__()
		self.intelligence = 20
		self.OptionSet = {
			BurningHands:{max:6,min:0,type:"arcane",range:1},
			LightningBolt:{max:4,min:0,type:"arcane",range:5}
			}
	
class Area(object):
	def __init_(self):
		self.tiles = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
					[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

class Options(object):
	def __init__(self):
		#arrows move
		#2. attack
			#A. melee targets available
			#B. ranged targets available
			#C. magic targets available

