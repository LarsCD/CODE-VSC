# main game file

# import modules
import random
import time
import datetime
import os
import sys
import pickle

# *** //// IMPORT FILES //// ***
# developer: this is  importing files but also managing errors and bugs
# developer: also logging data to a log file

time = datetime.datetime.now()
thisDir = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(thisDir, 'files/logFile')

logFile = open(filePath, 'a').close()
logFile = open(filePath, 'w').close()
logFile = open(filePath, 'a')
logFile.write('> SYSTEM: start main at ' + str(time) + '\n\n')
logFile.close()

try: 
	try: 
		from dev import *
	except ModuleNotFoundError:
		logFile = open(filePath, 'w+')
		logFile.write('\n> ERROR: ModuleNotFoundError: invalid dev file')
		logFile.close()
	dev.systemText('> SYSTEM: successfully imported dev file')
	from data import *
	dev.systemText('> SYSTEM: successfully imported data file')
	from settings import *
	dev.systemText('> SYSTEM: successfully imported settings file')
	from creatures import *
	dev.systemText('> SYSTEM: successfully imported creatures file')
	from items import *
	dev.systemText('> SYSTEM: successfully imported items file')
	from moves import *
	dev.systemText('> SYSTEM: successfully imported moves file')
	from graphics import *
	dev.systemText('> SYSTEM: successfully imported graphics file')
	from gameSequence import *
	dev.systemText('> SYSTEM: successfully imported gameSequence file')
	from cmdConfig import *
	dev.systemText('> SYSTEM: successfully imported cmdConfig file')
	from map import *
	dev.systemText('> SYSTEM: successfully imported map file')
	from npcData import *
	dev.systemText('> SYSTEM: successfully imported npcData file')
	from dialogues import *
	dev.systemText('> SYSTEM: successfully imported dialogues file')
	from locations import *
	dev.systemText('> SYSTEM: successfully imported locations file')
	from ascii import *
	dev.systemText('> SYSTEM: successfully imported ascii file')
	from scenes import *
	dev.systemText('> SYSTEM: successfully imported scenes file')
	if runOnPC == False:		
		try:
			import console			
		except ModuleNotFoundError:
			dev.errorText('\n> ERROR: ModuleNotFoundError')
			dev.errorText('> ERROR: invalid runOnPC config')
			dev.systemText('\n> SYSTEM: shutting down in 5 seconds')
			dev.systemText('\n> SYSTEM: application shutdown')
			time.sleep(5)
			sys.exit()			
except ModuleNotFoundError:
	dev.errorText('\n> ERROR: ModuleNotFoundError')
	dev.systemText('\n> SYSTEM: shutting down in 5 seconds')
	time.sleep(5)
	dev.systemText('\n> SYSTEM: application shutdown')
	sys.exit()

# dev.startUpMessage()

# *** //// DATA MANAGEMENT //// ***
class data:

	class moveData:
		def __init__(self, name, id, type, attack, defence, health, index, pp, maxpp):
			self.name = name
			self.id = id
			self.type = type
			self.attack = attack
			self.defence = defence
			self.health = health
			self.index = index
			self.PP = pp
			self.maxPP = maxpp
			t = datetime.datetime.now()
			dev.debugText('> DEBUG: ' + str(t) + ' >>> Loaded Move #' + str(id))

	class creatureData:
		def __init__(self, name, id, level, health, attack, defence, captureRate, moves):
			self.name = name
			self.id = id
			self.level = level
			self.health = health
			self.maxHealth = health
			self.attack = attack
			self.defence = defence
			self.captureRate = captureRate
			self.xp = 0
			self.xpMax = 10
			self.playerHasCreature = False
			self.playerIndex = 0
			moveList = []
			n = 0
			for number in moves:
				setMove = moveDataList[number]
				setMove['index'] = n
				n += 1
				moveList.append(setMove)
			self.moves = moveList
			t = datetime.datetime.now()
			dev.debugText('> DEBUG: ' + str(t) + ' >>> Loaded Creature #' + str(id))

	class itemData:
		def __init__(self, name, id, type, stats, price, stackable, rarity, spawnChance, keyItemCode, isBattleItem, description):
			self.name = name			
			self.id = id			
			self.type = type
			if type == 'healing_item':
				self.healing = stats
			if type  == 'capture_item':
				self.captureRate = stats
			if type == 'move_data':
				self.containedMove = stats
			if type == 'value_data':
				self.stats = None			
			self.price = price			
			self.stackable = stackable			
			self.playerHasItem = False						
			self.playerQuantity = 0			
			self.playerIndex = 0
			self.rarity = rarity
			self.spawnChance = spawnChance
			self.keyItemCode = keyItemCode
			self.isBattleItem = isBattleItem			
			t = datetime.datetime.now()
			dev.debugText('> DEBUG: ' + str(t) + ' >>> Loaded Item #' + str(id))

	class npcData:
		def __init__(self, name, id, gender, description, dialogue, firstInteraction):
			self.name = name
			self.id = id
			self.gender = genderList[gender]
			self.description = description
			self.dialogue = dialogue
			self.firstInteraction = firstInteraction
			self.index = 0
			t = datetime.datetime.now()
			dev.debugText('> DEBUG: ' + str(t) + ' >>> Loaded NPC #' + str(id))

	class structureData:
		def __init__(self, name, id, type, size, description, asciiSprite, npcs, creatureEncounters):
			self.name = name
			self.id = id
			self.type = type
			self.size = size
			self.description = description
			self.asciiSprite = asciiSprite
			npcList = []
			n = 0
			for number in npcs:
				setNpc = npcDataList[number]
				setNpc["index"] = n
				npcList.append(setNpc)
				n += 1
			self.npcs = npcList
			self.creatureEncounters = creatureEncounters
			self.index = 0
			t = datetime.datetime.now()
			dev.debugText('> DEBUG: ' + str(t) + ' >>> Loaded structure #' + str(id))

	class locationData:
		def __init__(self, name, id, type, description, asciiSprite, structures, paths, npcs, creatureEncounters):
			self.name = name
			self.id = id
			self.type = type
			self.description = description
			self.asciiSprite = asciiSprite
			structureList = []
			for number in structures:
				setStructure = structureDataList[number]
				structureList.append(setStructure)
			self.structures = structureList
			self.paths = paths
			npcList = []
			n = 0
			for number in npcs:
				setNpc = npcDataList[number]
				setNpc["index"] = n
				npcList.append(setNpc)
				# dev.debugText('\n> DEBUG: ' + str(npcList))
				n += 1
			self.npcs = npcList
			self.creatureEncounters = creatureEncounters
			t = datetime.datetime.now()
			dev.debugText('> DEBUG: ' + str(t) + ' >>> Loaded location #' + str(id))

	class playerData:
		def __init__(self, name, gender, locationID, money, creatureCount):
			self.name = name
			self.gender = gender
			self.locationID = 0
			self.money = money
			self.creatureCount = creatureCount
			t = datetime.datetime.now()
			dev.debugText('\n> DEBUG: ' + str(t) + ' >>> Loaded player')


class saveSystemAsset:

	def saveMoveData(moveData):
		global moveDataList
		moveDataList = moveData

	def saveCreatureData(creatureData):
		global creatureDataList
		creatureDataList = creatureData

	def saveItemData(itemData):
		global itemDataList
		itemDataList = itemData

	def saveNpcData(npcData):
		global npcDataList
		npcDataList = npcData

	def saveStructureData(structureData):
		global structureDataList
		structureDataList = structureData

	def saveLocationData(locationData):
		global locationDataList
		locationDataList = locationData

	def savePLayerData(playedDataInput):
		global playerData
		playerData = playedDataInput


class load:
	
	def loadMoveData():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> Start move load at ' + str(t))
		global globalMoveNumber, moveDataList
		list = []
		n = 0
		while n < globalMoveNumber:
			if n < 10:
				x = data.moveData(*(eval(str('m00' + str(n))))).__dict__
			elif n < 100:
				x = data.moveData(*(eval(str('m0' + str(n))))).__dict__
			elif n < 1000:
				x = data.moveData(*(eval(str('m' + str(n))))).__dict__
			list.append(x)
			n = n + 1
		moveDataList = list
		saveSystemAsset.saveMoveData(moveDataList)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		dev.systemText('> SYSTEM: move data loaded (loaded ' + str(globalMoveNumber) + ' assets) (' + str(ms) + 'ms)')
		
		
	def loadCreatureData():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> Start creature load at ' + str(t))
		global globalCreatureNumber, creatureDataList
		list = []
		n = 0
		while n < globalCreatureNumber:
			if n < 10:
				x = data.creatureData(*(eval(str('c00' + str(n))))).__dict__
			elif n < 100:
				x = data.creatureData(*(eval(str('c0' + str(n))))).__dict__
			elif n < 1000:
				x = data.creatureData(*(eval(str('c' + str(n))))).__dict__
			list.append(x)
			n = n + 1
		creatureDataList = list
		saveSystemAsset.saveCreatureData(creatureDataList)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		dev.systemText('> SYSTEM: creature data loaded (loaded ' + str(globalCreatureNumber) + ' assets) (' + str(ms) + 'ms)')
		
		
	def loadItemData():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> Start item load at ' + str(t))
		global globalItemNumber, itemDataList
		list = []
		n = 0
		while n < globalItemNumber:
			if n < 10:
				x = data.itemData(*(eval(str('i00' + str(n))))).__dict__
			elif n < 100:
				x = data.itemData(*(eval(str('i0' + str(n))))).__dict__
			elif n < 1000:
				x = data.itemData(*(eval(str('i' + str(n))))).__dict__
			list.append(x)
			n = n + 1
		itemDataList = list
		saveSystemAsset.saveItemData(itemDataList)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		dev.systemText('> SYSTEM: item data loaded (loaded ' + str(globalItemNumber) + ' assets) (' + str(ms) + 'ms)')
	
	
	def loadNpcData():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> Start npc load at ' + str(t))
		global globalNpcNumber, npcDataList
		list = []
		n = 0
		while n < globalNpcNumber:
			if n < 10:
				x = data.npcData(*(eval(str('npc00' + str(n))))).__dict__
			elif n < 100:
				x = data.npcData(*(eval(str('npc0' + str(n))))).__dict__
			elif n < 1000:
				x = data.npcData(*(eval(str('npc' + str(n))))).__dict__
			list.append(x)
			n = n + 1
		npcDataList = list
		saveSystemAsset.saveNpcData(npcDataList)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		dev.systemText('> SYSTEM: npc data loaded (loaded ' + str(globalNpcNumber) + ' assets) (' + str(ms) + 'ms)')
	
	
	def loadStructureData():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> Start structure load at ' + str(t))
		global globalStructureNumber, structureDataList
		list = []
		n = 0
		while n < globalStructureNumber:
			if n < 10:
				x = data.structureData(*(eval(str('s00' + str(n))))).__dict__
			elif n < 100:
				x = data.structureData(*(eval(str('s0' + str(n))))).__dict__
			elif n < 1000:
				x = data.structureData(*(eval(str('s' + str(n))))).__dict__
			list.append(x)
			n = n + 1
		structureDataList = list
		saveSystemAsset.saveStructureData(structureDataList)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		dev.systemText('> SYSTEM: structure data loaded (loaded ' + str(globalStructureNumber) + ' assets) (' + str(ms) + 'ms)')
	
	
	def loadLocationData():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> Start location load at ' + str(t))
		global globalLocationNumber, locationDataList
		list = []
		n = 0
		while n < globalLocationNumber:
			if n < 10:
				x = data.locationData(*(eval(str('l00' + str(n))))).__dict__
			elif n < 100:
				x = data.locationData(*(eval(str('l0' + str(n))))).__dict__
			elif n < 1000:
				x = data.locationData(*(eval(str('l' + str(n))))).__dict__
			list.append(x)
			n = n + 1
		locationDataList = list
		saveSystemAsset.saveLocationData(locationDataList)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		dev.systemText('> SYSTEM: location data loaded (loaded ' + str(globalLocationNumber) + ' assets) (' + str(ms) + 'ms)')

	def loadPlayer():
		playerDataList = (data.playerData(*(eval(str('playerInfo')))).__dict__)
		saveSystemAsset.savePLayerData(playerDataList)
		
	def loadGame():
		dev.clear()
		graphics.printLine()
		print(' LOADING...')
		graphics.printLine()
		print('\n' * (cmdLines - 6))
		graphics.printLine()
		lt = datetime.datetime.now()
		time.sleep(0.65)
		load.initializeColor()
		load.loadMoveData()
		load.loadCreatureData()
		load.loadItemData()
		load.loadNpcData()
		load.loadStructureData()
		load.loadLocationData()
		load.loadPlayer()
		lt2 = datetime.datetime.now()
		dTime = lt2 - lt
		s = round(float((dTime.total_seconds())), 2)
		allAssets = (globalCreatureNumber + globalItemNumber + globalMoveNumber + globalNpcNumber + globalStructureNumber + globalLocationNumber)
		dev.systemText('\n> SYSTEM: game loaded (loaded ' + (str(allAssets + 1)) + ' assets) (' + str(s) + 's)')
		dev.systemText('> SYSTEM: game load complete...\n\n')

	def initializeColor():
		t = datetime.datetime.now()
		dev.systemText('\n> SYSTEM: >>> colorInit at ' + str(t))
		cmd.color.defaultText('> textColor.def')
		cmd.color.greenText('> textColor.grn_b')
		cmd.color.yellowText('> textColor.ylw_b')
		cmd.color.redText('> textColor.red_b')
		cmd.color.blueText('> textColor.blu_b')
		cmd.color.magentaText('> textColor.mag_b')
		cmd.color.grayText('> textColor.gry')
		cmd.color.cyanText('> textColor.cya_b')
		cmd.color.orangeText('> textColor.org_b')
		dev.clear()
		# time.sleep(1)
		

# *** //// MAIN LOOP FUNCTIONS //// ***

class mainLoop():

	def gameLoop():
		while gameQuit == False:
			gameLocation.mainLocationLoop(locationDataList[playerData['locationID']])
		sys.exit()


# *** //// SYSTEM FUNCTIONS //// ***

class system:
	
	class pack:
		
		def packAllGameData():
			global allGameDataList
			allGameDataList = []			

			mainData = []
			mainData.append(creatureDataList)
			mainData.append(itemDataList)
			mainData.append(moveDataList)
			mainData.append(npcDataList)
			mainData.append(structureDataList)
			mainData.append(locationDataList)
			mainData.append(playerData)		
		
			creatureData = []
			creatureData.append(playerCreature)
			creatureData.append(currentCreature)
			creatureData.append(creatureBank)
			creatureData.append(creatureParty)
			creatureData.append(creatureDex)
			creatureData.append(creatureDexCount)

			inventoryData = []
			inventoryData.append(inventory)
			inventoryData.append(inventoryHealingItems)
			inventoryData.append(inventoryCaptureBalls)
			inventoryData.append(inventoryMoveItems)
			inventoryData.append(inventoryValueItems)

			allGameDataList.append(mainData)
			allGameDataList.append(creatureData)
			allGameDataList.append(inventoryData)
			# allGameDataList.append(setupData)
			# allGameDataList.append(playerData)
			# allGameDataList.append(battleData)
			# allGameDataList.append(moveData)
			# allGameDataList.append(locationData)
			# allGameDataList.append(npcsData)
			# allGameDataList.append(debugData)

			dev.systemText('\n> SYSTEM: all game data packaged')

	
	class save:
		
		def saveGame(fileName):
			global allGameDataList
			system.pack.packAllGameData()
			targetFile = open('saves/'+fileName, 'wb')
			pickle.dump(allGameDataList, targetFile)
			targetFile.close()
			dev.systemText('\n> SYSTEM: saved game data to ' + str(fileName))
			
			
		
	class load:
		
		def loadGame(fileName):
			t = datetime.datetime.now()
			# dev.systemText('\n> SYSTEM: start game data load')
			global allGameDataList
			targetFile = open('saves/'+fileName, 'rb')
			allGameDataList = pickle.load(targetFile)
			targetFile.close()
			# dev.systemText('\n> SYSTEM: stop game data load')
			system.load.loadDataLists()
			t2 = datetime.datetime.now()
			dTime = t2 - t
			ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
			dev.systemText('\n> SYSTEM: loaded game data from ' + str(fileName) + ' / (' + str(ms) + 'ms)')
			
			
		def loadDataLists(): 
			global creatureDataList, itemDataList, moveDataList, npcDataList, structureDataList, locationDataList, playerData
			creatureDataList = allGameDataList[0][0]
			itemDataList = allGameDataList[0][1]
			moveDataList = allGameDataList[0][2]
			npcDataList = allGameDataList[0][3]
			structureDataList = allGameDataList[0][4]
			locationDataList = allGameDataList[0][5]
			playerData = allGameDataList[0][6]



# *** //// MENU / SETTINGS FUNCTIONS //// ***

class menu:

	def startUpMenuLoop():
		dev.debugText('\n> DEBUG: running > menu.startUpMenuLoop()')
		os.system('mode con cols=120 lines=30')
		load.initializeColor()
		if debugMode == False:
			# print()
			dev.clear()
			scene.logo()
		global runGame
		runGame = False
		while runGame == False:
			menu.startUpMenu()
		cmd.settings.setResolution()
		load.loadGame()
		# mainLoop.gameLoop()

	def startUpMenu():
		dev.debugText('\n> DEBUG: running > menu.startUpMenu()')
		global runGame, gameQuit 
		graphics.system.startUpMenu()
		userInput = input('> INPUT: ')
		if userInput == 'c':
			runGame = True
		elif userInput == 's':
			menu.openMenuSettings()
		elif userInput == 'x':
			gameQuit = True
		else:
			pass

	def openMenuSettings():
		dev.debugText('\n> DEBUG: running > menu.openMenuSettings()')
		global runOnPC, debugMode, cmdCols, cmdLines
		graphics.system.startUpSettings(runOnPC, debugMode, cmdCols, cmdLines)
		userInput = input('> INPUT: ')
		if userInput == '1':
			if runOnPC == True:
				runOnPC = False
			else:
				runOnPC = True
			menu.openMenuSettings()
		elif userInput == '2':
			if debugMode == True:
				debugMode = False
			else:
				debugMode = True
			menu.openMenuSettings()
		elif userInput == '3':
			userInput1 = input('\n> Change cmdCols: ')
			cmdCols = userInput1
			menu.openMenuSettings()
		elif userInput == '4':
			userInput2 = input('\n> Change cmdLines: ')
			cmdLines = userInput2
			menu.openMenuSettings()
		elif userInput == 'x':
			pass
		else:
			pass
	
	def systemMenu():
		global exitToMain
		dev.clear()
		graphics.system.systemMenu()
		userInput = input('> INPUT: ')
		if userInput == 's':
			system.save.saveGame('game save')
		elif userInput == 'l':
			system.load.loadGame('game save')
		elif userInput == 'z':
			pass
		elif userInput == 'z':
			pass
		elif userInput == 'x': 
			exitToMain = True
		else:
			menu.systemMenu()
		


# *** //// LEVEL UP FUNCTIONS //// ***

class level:

	class levelUp:
		def __init__(self, name, id, level, health, maxHealth, attack, defence, captureRate, xp, xpMax, hasCreature, playerIndex, moves, levelUpNumber):
			self.name = name
			self.id = id
			self.level = level + levelUpNumber
			x = health + (random.randint(2, 4) * levelUpNumber)
			self.health = x
			self.maxHealth = x
			self.attack = attack + (random.randint(1, 3) * levelUpNumber)
			self.defence = defence + (random.randint(1, 3) * levelUpNumber)
			self.captureRate = captureRate
			self.xp = xp
			self.xpMax = (xpMax + round(xpMax + (xpMax * 0.2)) * levelUpNumber)
			self.playerHasCreature = hasCreature
			self.playerIndex = playerIndex
			self.moves = moves

	def saveLevelUpCreatureData(currentCreature):
		creatureDataList[currentCreature['id']] = currentCreature

	def updateCurrentCreatureData(updatedCurrentCreature):
		global creatureDataList
		targetCreature = updatedCurrentCreature
		creatureDataList[updatedCurrentCreature['id']] = updatedCurrentCreature
		
		# global currentCreature, enemyCreature
		# currentCreature = updatedCurrentCreature
		# if currentCreature == enemyCreature:
		# 	enemyCreature = updatedCurrentCreature

	def updateBattleXP(enemyCreature):
		global creatureDataList
		creatureID = playerCreature['id'] 
		targetCreature = creatureDataList[creatureID]
		levelUp = False
		xpAdd = round(random.randint((int(enemyCreature['level']) - 1), (int(enemyCreature['level']) - 1)) * (xpMultiplier * 10))
		dev.debugText('\n> DEBUG: ' + targetCreature['name'] + ': xpAdd = ' + str(xpAdd))
		targetCreature['xp'] = (targetCreature['xp'] + xpAdd)
		if targetCreature['xp'] >= targetCreature['xpMax']:
			levelUp = True
			targetCreature['xp'] = targetCreature['xp'] - targetCreature['xpMax']
			creature.levelUpCreature(targetCreature, 1)
			creature.updatePlayerCreature(targetCreature)
		graphics.xpAddDisplay(playerCreature, xpAdd, levelUp)

	def addXP(creatureInput, xpAdd):
		global creatureDataList
		creatureID = creatureInput['id'] 
		targetCreature = creatureDataList[creatureID]
		levelUp = False
		dev.debugText('\n> DEBUG: ' + targetCreature['name'] + ': xpAdd = ' + str(xpAdd))
		targetCreature['xp'] = (targetCreature['xp'] + xpAdd)
		if targetCreature['xp'] >= targetCreature['xpMax']:
			levelUp = True
			targetCreature['xp'] = targetCreature['xp'] - targetCreature['xpMax']
			creature.levelUpCreature(targetCreature, 1)
			creature.updatePlayerCreature(targetCreature)
	
	def checkLevelUp(creature):
		global creatureDataList
		targetCreature = creatureDataList[creature['id']]


# *** //// BATTLE FUNCTIONS 2.0 //// ***

class battle:

	def begin():
		dev.debugText('\n> DEBUG: running > battle.begin()')
		global playerCreature, battleOver
		playerCreature = creatureParty[0]
		enemyCreature['health'] = enemyCreature['maxHealth']
		battleOver = False
		battle.battleLoop()
		
		
	def checkHealth():
		dev.debugText('\n> DEBUG: running > battle.checkHealth()')
		global battleOver, battleEndCode
		if playerCreature['health'] <= 0:
			n = 0
			for creature in creatureParty:
				if creature['health'] <= 0:
					n += 1
			if len(creatureParty) == n:
				if enemyCreature['health'] <= 0:
					battleOver = True
					battleEndCode = 4
				else:
					battleOver = True
					battleEndCode = 3
			else:
				battle.faintedCreatureSwitch()
				battleOver = False
			dev.debugText('\n> DEBUG: battleOver = ' + str(battleOver))
		if enemyCreature['health'] <= 0:
			battleOver = True
			battleEndCode = 2
			dev.debugText('\n> DEBUG: battleOver = ' + str(battleOver))
			
			
	def battleLoop():
		dev.debugText('\n> DEBUG: running > battle.battleLoop()')
		global battleOver
		battle.checkHealth()
		while battleOver == False:
			battle.checkHealth()
			if battleOver == True:
				break
			battle.playerInput()
		dev.debugText('\n> DEBUG: battleDone')
		if battleEndCode == 0: # Run
			dev.clear()
			graphics.printLine()
			print('\n > Player ran away')
			time.sleep(2)
		elif battleEndCode == 1: # Captured
			# print('\n> Player captured Creature')
			# time.sleep(2)
			creature.addCreature(enemyCreature)
			battle.battleLoop()
			# print('\n\'' + enemyCreature['name'] + '\' (#' + str(enemyCreature['id']) + ')')
		elif battleEndCode == 2: # Enemy Creature fainted
			# print('\n> Enemy creature fainted')
			# time.sleep(2)
			sequence.battle.battleOverSeq(enemyCreature, battleEndCode)
			battle.getReward(enemyCreature)
			# time.sleep(2)
		elif battleEndCode == 3: # Player Creature fainted
			# print('\n> Player creature fainted')
			# time.sleep(2)
			sequence.battle.battleOverSeq(enemyCreature, battleEndCode)
		elif battleEndCode == 4: # Both Creatures fainted
			# print('\n> Both creatures fainted')
			# time.sleep(2)
			sequence.battle.battleOverSeq(enemyCreature, battleEndCode)
			
		
		
	def playerInput():
		dev.debugText('\n> DEBUG: running > battle.playerInput()')
		battle.checkEndBattle()
		if battleOver == True:
			pass
		else:
			dev.debugText('\n> DEBUG: <mainBattle>')
			dev.debugText('\n> DEBUG: pTurnDone = ' + str(playerTurnDone))
			dev.debugText('\n> DEBUG: playerInput / battleOver=' + str(battleOver))
			dev.clear()
			graphics.enemyCreatureGUID(enemyCreature)
			graphics.playerCreatureGUID(playerCreature)
			graphics.battleChoice2GUID()
			
			userInput = input('\n> INPUT: ')
			if userInput == 'f':
				userInput = None
				battle.movesMenu()
			elif userInput == 'c':
				battle.creatureParty()
			elif userInput == 'i':
				battle.inventoryMenu()
			elif userInput == 'r':
				battle.runOption()
			else:
				dev.errorText('\n> ERROR: invalid input')
			battle.checkEndBattle()
			# dev.debugText('\n> DEBUG: playerInput / battleOver=' + str(battleOver))
			if battleOver == True:
				pass
			else:
				if playerTurnDone == True:
					dev.debugText('\n> DEBUG: enemyTurn')
					battle.enemyMove()
					battle.battleEvent()
					
					
	def checkEndBattle():
		dev.debugText('\n> DEBUG: running > battle.checkEndBattle()')
		global battleOver
		dev.debugText('\n> DEBUG: battleOver=' + str(battleOver))
		battle.checkHealth()
		if enemyCreature in creatureDex:
			battleOver = True
		return battleOver
		
		
		
	def enemyMove():
		# redesign later to Enemy AI
		dev.debugText('\n> DEBUG: running > battle.enemyMove()')
		global enemyRoundChoice, enemyRoundStats
		dev.debugText('\n> DEBUG: <enemyMove>')
		moveNumber = len(enemyCreature['moves'])
		randomMoveIndex = random.randint(0, (moveNumber - 1))
		dev.debugText('\n> DEBUG: enemy move index = ' + str(randomMoveIndex))
		enemyMove = enemyCreature['moves'][randomMoveIndex]
		enemyRoundChoice = enemyMove['type']
		enemyRoundStats = enemyMove[moveTypeName[enemyMove['type']]]
		dev.debugText('\n> DEBUG: enemy move = ' + enemyMove['name'])
		dev.debugText('\n> DEBUG: enemy choice: ' + enemyRoundChoice)
		dev.debugText('\n> DEBUG: enemy stats: ' + str(enemyRoundStats))
		
		
	def battleEvent(): 
		# FUCKING REDESIGN THIS, ITS HORRORIBLE, LIKE, FUCKING LOOK AT IT!!!!!!!!!!
		# You ungratefull piece of shit "programmer"............
		dev.debugText('\n> DEBUG: running > battle.battleEvent()')
		global playerRoundChoice, playerRoundStats, enemyRoundChoice, enemyRoundStats
		dev.clear()
		graphics.enemyCreatureGUID(enemyCreature)
		graphics.playerCreatureGUID(playerCreature)
		graphics.printLine()
		print(' [Battle]')
		pAtk = 0
		pDef = 0
		pHp = 0
		eAtk = 0
		eDef = 0
		eHp = 0
		time.sleep(0.5)
		if playerRoundChoice == 'atk':
			pAtk = playerRoundStats
			print('\n > Player is attacking: ' + str(pAtk) + ' attack')
		elif playerRoundChoice == 'def':
			pDef = playerRoundStats
			print('\n > Player is defending: ' + str(pDef) + ' defence')
		elif playerRoundChoice == 'hp':
			pHp = playerRoundStats
			print('\n > Player is healing: +' + str(pHp) + ' HP')
		elif playerRoundChoice == 'itm':
			pItm = playerRoundStats
			print('\n > Player used item: +' + str(pItm) + (' HP'))
		time.sleep(2)
		if enemyRoundChoice == 'atk':
			eAtk = enemyRoundStats
			print('\n > Enemy is attacking: ' + str(eAtk) + ' attack')
		elif enemyRoundChoice == 'def':
			eDef = enemyRoundStats
			print('\n > Enemy is defending: ' + str(eDef) + ' defence')
		elif enemyRoundChoice == 'hp':
			eHp = enemyRoundStats
			print('\n > Enemy is healing: +' + str(eHp) + ' HP')
		elif enemyRoundChoice == 'itm':
			eItm = enemyRoundStats
			print('\n > Enemy used item: +' + str(eItm) + (' HP'))
			
		if pDef > eAtk:
			pDef = eAtk
		if eDef > pAtk:
			eDef = pAtk
		time.sleep(3)
		
		playerRoundChoice = None
		playerRoundStats = None
		enemyRoundChoice = None
		enemyRoundStats = None
		battle.updateDamage(pAtk, pDef, pHp, eAtk, eDef, eHp)
		
		
	def updateDamage(pAtk, pDef, pHp, eAtk, eDef, eHp):
		dev.debugText('\n> DEBUG: running > battle.updateDamage()')
		global playerCreature, enemyCreature
		playerCreature['health'] -= eAtk - pDef - pHp
		enemyCreature['health'] -= pAtk - eDef - eHp
		if playerCreature['health'] < 0:
			playerCreature['health'] = 0
		elif playerCreature['health'] > playerCreature['maxHealth']:
			playerCreature['health'] = playerCreature['maxHealth']
		if enemyCreature['health'] < 0:
			enemyCreature['health'] = 0
		elif enemyCreature['health'] > enemyCreature['maxHealth']:
			enemyCreature['health'] = enemyCreature['maxHealth']


	def movesMenu():
		dev.debugText('\n> DEBUG: running > battle.movesMenu()')
		dev.clear()
		graphics.enemyCreatureGUID(enemyCreature)
		graphics.playerCreatureGUID(playerCreature)
		moves = playerCreature['moves']
		graphics.usePlayerMoves(playerCreature, moves)
		userInput = input('\n> INPUTmov: ')
		# check if int, otherwise search for string input
		isInt = None
		try:
			userInput = int(userInput)
			isInt = True
		except ValueError:
			isInt = False
		# exection
		if isInt == False:
			if userInput == 'q':
				battle.playerInput()
			else:
				dev.errorText('\n> ERROR: invalid input')
				battle.movesMenu()
		else:
			targetMoveIndex = (int(userInput) - 1)
			for move in moves:
				if move['index'] == targetMoveIndex:
					targetMove = move
					break
				else:
					targetMove = None
			if targetMove == None:
				dev.errorText('\n> ERROR: invalid input')
			else:
				if targetMove['PP'] == 0:
					print('\n > Cannot use this move anymore, no PP left')
					time.sleep(2)
					battle.movesMenu()
				else:
					battle.moveManagement(targetMove, targetMove['type'])
			
			
	def moveManagement(targetMove, targetMoveType):
		dev.debugText('\n> DEBUG: running > battle.moveManagement()')
		global playerTurnDone, playerRoundChoice, playerRoundStats
		playerRoundChoice = targetMoveType
		playerRoundStats = targetMove[moveTypeName[targetMoveType]]
		playerTurnDone = True
		targetMove['PP'] -= 1
		if targetMove['PP'] < 0:
			targetMove['PP'] = 0
		dev.debugText('\n> DEBUG: player choice: ' + playerRoundChoice)
		dev.debugText('\n> DEBUG: player stats: ' + str(playerRoundStats))
		

	def creatureParty():
		dev.debugText('\n> DEBUG: running > battle.creatureParty()')
		dev.clear()
		graphics.enemyCreatureGUID(enemyCreature)
		graphics.playerCreatureGUID(playerCreature)
		graphics.printLine()
		graphics.creaturePartyDisplay(creatureParty, playerCreature)
		print(' [' + textColor['grn_b'] + 's' + textColor['wht_b'] + '] : Switch Creature')
		print(' [' + textColor['grn_b'] + 'q' + textColor['wht_b'] + '] : Quit')
		graphics.printLine()
		userInput = input('> INPUT: ')
		if userInput == 's': 
			dev.clear()
			graphics.enemyCreatureGUID(enemyCreature)
			graphics.playerCreatureGUID(playerCreature)
			graphics.printLine()
			graphics.creaturePartyDisplay(creatureParty, playerCreature)
			userInput2 = input('\n> Select Creature to Switch: ')
			err = False
			try:
				targetCreature = creatureParty[int(userInput2) - 1]
			except:
				dev.errorText('\n> ERROR: invalid input')
				err = True
			if err == True:
				pass
			else:
				if targetCreature['health'] <= 0:
					print('\n > Cannot switch to fainted creature')
					time.sleep(2)
					battle.creatureParty()
				else:
					creature.switchCreatureInParty(targetCreature)
		elif userInput == 'q':
			pass
		else:
			battle.creatureParty()
			

	def inventoryMenu():
		dev.debugText('\n> DEBUG: running > battle.inventoryMenu()')
		dev.clear()
		graphics.enemyCreatureGUID(enemyCreature)
		graphics.playerCreatureGUID(playerCreature)
		inventory.usePlayerInventory(inventoryHealingItems, inventoryCaptureBalls)
		userInput = input('\n> INPUT: ')
		# check if int, otherwise search for string input
		isInt = None
		try:
			userInput = int(userInput)
			targetItemIndex = (int(userInput) - 1)
			isInt = True
		except ValueError:
			isInt = False
		# exection
		targetItem = None
		if isInt == False:
			if userInput == 'q':
				battle.playerInput()
			else:
				dev.errorText('\n> ERROR: invalid input')
				battle.inventoryMenu()
		else:
			for item in playerInventory:
				if item['playerIndex'] == targetItemIndex:
					targetItem = item
					break
				else:
					targetItem = None
			if targetItem == None:
				battle.inventoryMenu()
			else:
				dev.debugText('\n> DEBUG: targetItem= ' + str(targetItem['name']))
				if targetItem['type'] == 'healing_item':
					battle.itemManagement(targetItem, targetItem['type'])
				elif targetItem['type'] == 'capture_item':
					battle.itemManagement(targetItem, targetItem['type'])
				else:
					print('\n > Cannot use this item in battle')
			
			
	def itemManagement(targetItem, itemType):
		# //// REDESIGN!!!!!!!
		dev.debugText('\n> DEBUG: running > battle.itemManagement()')
		global playerCreature, playerTurnChoice, playerRoundChoice, playerRoundStats, playerTurnDone
		if itemType == 'healing_item':
			dev.clear()
			graphics.enemyCreatureGUID(enemyCreature)
			graphics.playerCreatureGUID(playerCreature)
			graphics.itemDisplay(targetItem)
			graphics.printLine()
			print(' [' + textColor['grn_b'] + 'y' + textColor['wht_b'] + '] : Yes')
			print(' [' + textColor['red_b'] + 'n' + textColor['wht_b'] + '] : No')
			userInput = input('\nDo you wanna use this item? ')
			if userInput == 'y':
				if playerCreature['health'] == playerCreature['maxHealth']:
					print('\n > Player creature health already full...')
					time.sleep(2)
				else:
					try:
						targetCreature = playerCreature
					except ValueError:
						dev.errorText('\n> ERROR: targetIndex not right')
					creature.healCreature(targetCreature, targetItem['healing'])
					inventory.removeFromInventory(targetItem['id'], 1)
					playerRoundChoice = 'itm'
					playerRoundStats = targetItem['healing']
					playerTurnDone = True
			elif userInput == 'n':
				pass
		elif itemType == 'capture_item':
			dev.clear()
			graphics.enemyCreatureGUID(enemyCreature)
			graphics.playerCreatureGUID(playerCreature)
			graphics.itemDisplay(targetItem)
			graphics.printLine()
			print(' [' + textColor['grn_b'] + 'y' + textColor['wht_b'] + '] : Yes')
			print(' [' + textColor['red_b'] + 'n' + textColor['wht_b'] + '] : No')
			userInput = input('\nDo you wanna use this item? ')
			if userInput == 'y':
				creature.captureEnemyCreature(enemyCreature, targetItem)
				inventory.removeFromInventory(targetItem['id'], 1)
				playerTurnDone = True
			elif userInput == 'n':
				playerTurnDone = False
		else:
			dev.errorText('\n> ERROR: invalid input')
				
				
	def runOption():
		dev.debugText('\n> DEBUG: running > battle.runOption()')
		global battleOver, battleEndCode
		battleOver = True
		battleEndCode = 0
	
	def getReward(enemyCreature):
		cLevel = enemyCreature['level']
		cCaptureRate = enemyCreature['captureRate']
		level.updateBattleXP(enemyCreature)
		# 				 level            cap.rate
		reward = round((((cLevel * 2) * 10) / (cCaptureRate * 2) + random.randint(0, 20)) * 10)
		sequence.battle.rewardsSeq(reward)
		inventory.addMoney(reward)
	
	def faintedCreatureSwitch():
		dev.clear()
		graphics.enemyCreatureGUID(enemyCreature)
		graphics.playerCreatureGUID(playerCreature)
		graphics.printLine()
		print('\n > ' + playerCreature['name'] + ' fainted...\n')
		time.sleep(2)
		graphics.printLine()
		graphics.creaturePartyDisplay(creatureParty, playerCreature)
		print(' > Select a creature to switch')
		userInput = input('\n> INPUT: ')
		err = False
		try:
			targetCreature = creatureParty[int(userInput) - 1]
		except:
			dev.errorText('\n> ERROR: invalid input')
			err = True
		if err == True:
			pass
		else:
			if targetCreature['health'] <= 0:
				dev.clear()
				graphics.enemyCreatureGUID(enemyCreature)
				graphics.playerCreatureGUID(playerCreature)
				graphics.printLine()
				print('\n > Cannot switch to fainted creature')
				time.sleep(2)
				battle.faintedCreatureSwitch()
			else:
				creature.switchCreatureInParty(targetCreature)


# *** //// ENCOUNTER //// ***

def testEncounter():
	global enemyCreature
	encounterIndex = random.randint(0, int(globalCreatureNumber - 1))
	if creatureDataList[encounterIndex] in creatureBank or creatureDataList[encounterIndex] in creatureParty:
		dev.debugText('\n> DEBUG: encounter creature already in bank')
		testEncounter()
	else:
		dev.clear()
		#encounterCreature = creatureDataList[encounterIndex]
		creature.levelUpCreature(creatureDataList[encounterIndex], 14)
		enemyCreature = creatureDataList[encounterIndex]
		dev.debugText('\n> DEBUG: encCreature: ' + str(enemyCreature['name'] + ' (#' + str(enemyCreature['id'])) + ')')
		graphics.printLine()
		cmd.color.redText('\n\n> A wild creature appeared...')
		time.sleep(2)
		battle.begin()


# *** //// INVENTORY //// ***

class inventory:

	def addToInventory(targetItem, quantity):
		# adds item to inventory
		global playerInventory, itemDataList, globalItemNumber
		targetID = targetItem['id']
		# item management
		# dev.debugText('\n> DEBUG: targetItem=' + str(targetItem))
		if targetItem in playerInventory:
			if targetItem['stackable'] == True:
				targetItem['playerQuantity'] = targetItem['playerQuantity'] + quantity
			else:
				dev.errorText('\n> ERROR: non-stackable item with id: ', str(targetID), ' already in inventory')
		else:
			if targetItem['stackable'] == True:
				targetItem['playerQuantity'] = quantity
				targetItem['playerHasItem'] = True
				playerInventory.append(targetItem)
			else:
				if quantity > 1:
					dev.errorText('\n> ERROR: item is not stackable, adding with quantity 1')
					quantityInput = 1
					targetItem['playerQuantity'] = quantity
					targetItem['playerHasItem'] = True
					playerInventory.append(targetItem)
				else:
					targetItem['playerQuantity'] = quantity
					targetItem['playerHasItem'] = True
					playerInventory.append(targetItem)
		dev.debugText('\n> DEBUG: added ' + targetItem['name'] + ' to inventory (' + str(quantity) + 'x)')
		inventory.sortInventory()


	def removeFromInventory(targetID, quantity):
		# removes item from inventory
		global playerInventory
		for item in playerInventory:
			if item['id'] == targetID:
				targetItem = item
				targetItem['playerQuantity'] -= quantity
				if targetItem['playerQuantity'] < 1:
					targetItem['playerQuantity'] = 0
					dev.debugText('\n> DEBUG: removed ' + targetItem['name'] + ' from inventory completly')
				dev.debugText('\n> DEBUG: removed ' + targetItem['name'] + ' from inventory (' + str(quantity) + 'x)')
		inventory.sortInventory()


	def sortInventory():
		# sorts for item in inventory
		global playerInventory, inventoryHealingItems, inventoryCaptureBalls
		for item in playerInventory:
			targetInventory = itemInventoryType[item['type']]
			if item['playerQuantity'] == 0:
				item['playerHasItem'] = False
				item['playerIndex'] = 0
				playerInventory.remove(item)
				targetInventory.remove(item)
				inventory.updateInventoryIndex()
				inventory.sortInventory()
			else:
				if item in targetInventory:
					item['playerHasItem'] = True
				else:
					targetInventory.append(item)
					item['playerHasItem'] = True
		inventory.updateInventoryIndex()


	def updateInventoryIndex():
		# updated item 'playerIndex'
		idList = []
		for item in playerInventory:
			idList.append(item['id'])
			idList.sort()
		for item in playerInventory:
			indexPos = idList.index(item['id'])
			item['playerIndex'] = indexPos
		inventory.updateInventoryOrder()


	def updateInventoryOrder():
		# sets order of items from low to high index (with magic)
		for item in playerInventory:
			targetInventory = itemInventoryType[item['type']]
			sortKey = lambda targetInventory: targetInventory['id']
			newTargetInventory = targetInventory.sort(key=sortKey)
			targetInventory = newTargetInventory


	def itemUse(item):
		# applies target item
		if item['type'] == 'healing_item':
			if playerCreature['health'] != playerCreature['maxHealth']:
				creature.healCreature(playerCreature, item['healing'])
				inventory.removeFromInventory(item, 1)
			else:
				print('\n > Creature is full health')
		if item['type'] == 'capture_item':
			print('\n > Cannot use this item right now...')
			time.sleep(2)
		targetInventory = itemInventoryType[item['type']]


	def usePlayerInventory(inventoryHealingItems, inventoryCaptureBalls):
		inventory.sortInventory()
		graphics.usePlayerInventory(inventoryHealingItems, inventoryCaptureBalls)
	
	def addMoney(money):
		global playerData
		playerData['money'] += money	



# *** //// PLAYER FUNCTIONS //// ***

class player:

	def useInventory():
		dev.clear()
		usePlayerInventory(inventoryHealingItems, inventoryCaptureBalls)
		
		userInput = input('\n> INPUT: ')
		try:
			userInput = int(userInput)
		except:
			pass
		if isinstance(userInput, int) == True:
			if int(userInput) > len(playerInventory):
				dev.errorText('\n> ERROR: item does exist not in inventory')
				time.sleep(2)
				player.useInventory()
			else:
				targetItem = playerInventory[(int(userInput) - 1)]
				dev.clear()
				graphics.itemDisplay(targetItem)
				graphics.printLine()
				print(' [y] : Yes')
				print(' [n] : No')
				userInput = input('\nDo you wanna use this item? ')
				if userInput == 'y':
					itemUse(targetItem)
				elif userInput == 'n':
					player.useInventory()
				else:
					dev.errorText('\n> ERROR: invalid input')
					time.sleep(2)
					player.useInventory()
		else:
			if userInput == 'q':
				pass
			else:
				dev.errorText('\n> ERROR: Invalid input')
				time.sleep(2)
				player.useInventory()

				
	def useCreatureDex(creatureDex, creatureDataList):
		graphics.useCreatureDexP1(creatureDex, creatureDataList)
		userInput = input()
		graphics.useCreatureDexP2(creatureDex, creatureDataList)
		userInput = input()
		graphics.useCreatureDexP3(creatureDex, creatureDataList)
		userInput = input()
		graphics.useCreatureDexP4(creatureDex, creatureDataList)
		userInput = input()

	def openMap():
		map.drawTestMap()
		


# *** //// CREATURE FUNCTIONS //// ***

class creature:

	def levelUpCreature(currentCreature, levelUpNumber):
		currentCreature = level.levelUp(*currentCreature.values(), levelUpNumber).__dict__
		level.saveLevelUpCreatureData(currentCreature)
		dev.debugText('> DEBUG: creature \'' + str(currentCreature['name']) + '\' leveled up by ' + str(levelUpNumber) + ' levels')
		dev.debugText('> DEBUG: creature \'' + str(currentCreature['name']) + '\' now level ' + str(currentCreature['level']) + '\n')
		updatedCurrentCreature = currentCreature
		level.updateCurrentCreatureData(updatedCurrentCreature)
		creature.updateMoves(updatedCurrentCreature)

	def healCreature(targetCreature, healing):
		targetCreature['health'] += healing
		if targetCreature['health'] > targetCreature['maxHealth']:
			targetCreature['health'] = targetCreature['maxHealth']
		dev.debugText('\n> DEBUG: healed ' + targetCreature['name'] + ' (id: ' + str(targetCreature['id']) + ') ' + '(+ ' + str(healing) + 'HP)')
		time.sleep(2)
		
	def recoverCreature(creature):
		global creatureDataList 
		targetCreature = creatureDataList[creature['id']]
		targetCreature['health'] == targetCreature['maxHealth']
		for move in targetCreature['moves']:
			move['PP'] = move['maxPP']
					
	def addCreature(targetCreature):
		global creatureParty, creatureBank
		if targetCreature in creatureParty:
			dev.errorText('\n> ERROR: creature already in party')
		else:
			if targetCreature in creatureBank:
				dev.errorText('\n> ERROR: creature already in bank')
			else:
				if len(creatureParty) >= maxCreatureParty:
					creature.addToBank(targetCreature)
				else:
					creature.addToParty(targetCreature)
				creature.addToCreatureDex(targetCreature)
				
				
	def addToCreatureDex(targetCreature):
		global creatureDex, creatureDexCount
		if targetCreature in creatureDex:
			pass
		else:
			creatureDex.append(targetCreature)
			playerData['creatureCount'] += 1
			creature.sortCreatureIndex(creatureDex)
		creatureDexCount = len(creatureDex) 
		dev.debugText('> DEBUG: ' + str(creatureDexCount) + ' creatures known / in CreatureDex')
			
			
	def addToParty(targetCreature):
		if targetCreature in creatureParty:
			print('\n > creature already in party')
		elif len(creatureParty) >= maxCreatureParty:
			print('\n > creature party full')
		else:
			creatureParty.append(targetCreature)
			print('\n > Added creature \'' + targetCreature['name'] + '\' (#' + str(targetCreature['id']) + ') to Creature Party')
			
			
	def addToBank(targetCreature):
		if targetCreature in creatureBank:
			print('\n > creature already in creature bank')
		else:
			targetCreature['health'] == targetCreature['maxHealth']
			creatureBank.append(targetCreature)
			creature.sortCreatureIndex(creatureBank)
			print('\n > Added creature \'' + targetCreature['name'] + '\' (#' + str(targetCreature['id']) + ') to Creature Bank')
			
			
	def captureEnemyCreature(enemyCreature, captureItem):
		itemCaptureRate = captureItem['captureRate']
		A = captureItem['captureRate']
		Hmax = enemyCreature['maxHealth']
		Hnow = enemyCreature['health']
		Lvl = enemyCreature['level']
		C = enemyCreature['captureRate']
		if captureItem['name'] == 'Master Capture Ball':
			isCaptured = True
			percentage = 100
		else:
			# some calculations for capturing (idk how tho)
			# also remove the dev.debugText()'s
			N = round((Hmax / Hnow) * C / 10 * 2)
			dev.debugText('N=' + str(N))
			X = A*0.01
			dev.debugText('X=' + str(X))
			dev.debugText('N/X='+ str(N/X))
			percentage = (N/A) * (100 + Lvl)
			if N/X >= A:
				isCaptured = True
				dev.debugText('Capture')
			else:
				isCaptured = False
				dev.debugText('No capture')
		dev.clear()
		graphics.enemyCreatureGUID(enemyCreature)
		graphics.playerCreatureGUID(playerCreature)
		sequence.battle.captureSeq(enemyCreature, captureItem, isCaptured, percentage)		
		if isCaptured == True:			
			creature.addCreature(enemyCreature)
			time.sleep(3)
			dev.clear()			
			graphics.creatureDisplay(enemyCreature)			
			print(' [' + textColor['grn_b'] + 'enter' +  textColor['wht_b'] + '] : Continue')
			graphics.printLine()
			input1 = input()
			graphics.shortCreatureDexDisplay(creatureDex, creatureDataList, enemyCreature)
			user = input()
			battleEndCode = 1
			
	def sortCreatureIndex(targetList):
		# updated creature 'playerIndex' (with magic)
		idList = []
		for creat_ in targetList:
			idList.append(creat_['id'])
			idList.sort()
		for creat_ in targetList:
			indexPos = idList.index(creat_['id'])
			creat_['playerIndex'] = indexPos
		for creature in targetList:
			sortKey = lambda targetList: targetList['id']
			targetList.sort(key=sortKey)
			
			
	def switchCreatureInParty(targetCreature):
		# switches targetCreature with current playerCreature
		global creatureParty, playerCreature
		if targetCreature in creatureParty:
			if playerCreature in creatureParty:
				dev.debugText('> DEBUG: playerCreature: #' + str(playerCreature['id']))
				dev.debugText('> DEBUG: targetCreature: #' + str(targetCreature['id']))
				targetCreature, playerCreature = playerCreature, targetCreature
				dev.debugText('\n> DEBUG: \'' + playerCreature['name'] + '\' (#' + str(playerCreature['id']) + ') now current creature, \'' + targetCreature['name'] + '\' (#' + str(targetCreature['id']) + ') now in creatureParty\n')
				# print('\n> \'' + playerCreature['name'] + '\' (#' + str(playerCreature['id']) + ') now current creature, \'' + targetCreature['name'] + '\' (#' + str(targetCreature['id']) + ') now in creatureParty\n')
				# time.sleep(3)
		# graphics.useCreatureParty(playerCreature)
			elif playerCreature == None:
				dev.errorText('\n> ERROR: playerCreature not set (NoneType)')
			else:
				dev.errorText('\n> ERROR: playerCreature not in creatureParty')
		else:
			dev.errorText('\n> ERROR: targetCreature not in creatureParty')

	def updatePlayerCreature(creature):
		global playerCreature
		global creatureDataList
		playerCreature = creatureDataList[creature['id']]
	
	
	def updateMoves(creature):
		global creatureDataList
		targetCreature = creature
		statLevelAdd = int(round(targetCreature['level'] / 10))
		for move in targetCreature['moves']:
			stat = moveTypeName[move['type']]
			statAdd = int(round(targetCreature[stat] / 20))
			newMoveStat = move[stat] + int(statAdd + statLevelAdd)
			# targetCreature['moves'][move['id']][stat] = int(newMoveStat)
		creatureDataList[targetCreature['id']] = targetCreature
		dev.debugText('\n> DEBUG: moves updated for creature #' + str(targetCreature['id']))
	


# *** //// LOCATION FUNCTIONS //// ***

class gameLocation:
		
	def mainLocationLoop(location):
		dev.debugText('\n> DEBUG: running > gameLocation.mainLocationLoop()')
		global exitLocation
		exitLocation = False
		while exitLocation == False:
			gameLocation.showLocationMenu(location)
			playerData['locationID'] = location['id']
	
	def loadLocation(locationID):
		dev.debugText('\n> DEBUG: running > gameLocation.loadLocation()')
		gameLocation.mainLocationLoop(locationDataList[locationID])

	def showLocationMenu(location):
		dev.debugText('\n> DEBUG: running > gameLocation.showLocationMenu()')
		global exitLocation
		graphics.location.locationMenu(location)
		userInput = input('> INPUT: ')
		if userInput == 'p':
			gameLocation.showPlayerMenu(location)
		elif userInput == 'e':
			gameLocation.showExploreMenu(location)
		elif userInput == 'i':
			gameLocation.showInformationMenu(location)
		elif userInput == 't':
			exitLocation = True
		elif userInput == 'x':
			menu.systemMenu()
		else: 
			pass
	
	def showPlayerMenu(location):
		dev.debugText('\n> DEBUG: running > gameLocation.showPlayerMenu()')
		graphics.location.playerMenu(location, playerData)
		userInput = input('> INPUT: ')
		if userInput == 'p':
			gameLocation.subMenus.playerInfoDisplay(location, playerData)
		elif userInput == 'c':
			gameLocation.subMenus.playerCreatureParty(location)
		elif userInput == 'i':
			gameLocation.subMenus.playerInventory(location, inventoryHealingItems, inventoryCaptureBalls)
		elif userInput == 'd':
			gameLocation.subMenus.playerCreatureDex(location, creatureDex)
		elif userInput == 'm':
			gameLocation.subMenus.playerMap(location)
		elif userInput == 'e':
			pass
		else: 
			gameLocation.showPlayerMenu(location)
	
	def showExploreMenu(location):
		dev.debugText('\n> DEBUG: running > gameLocation.showExploreMenu()')
		graphics.location.exploreMenu(location)
		userInput = input('> INPUT: ')
		if userInput == 'g':
			gameLocation.subMenus.exploreGoTo(location)
		elif userInput == 't':
			gameLocation.subMenus.exploreTalkTo(location)
		elif userInput == 's':
			loot.startLoot()
			gameLocation.showExploreMenu(location)
		elif userInput == 'e':
			pass
		else: 
			gameLocation.showExploreMenu(location)
	
	def showInformationMenu(location):
		dev.debugText('\n> DEBUG: running > gameLocation.showInformationMenu()')
		graphics.location.informationMenu(location)
		userInput = input('> INPUT: ')
		if userInput == 'e':
			pass
		else: 
			gameLocation.showInformationMenu(location)
	
	def showSystemMenu():
		menu.systemMenu()
	
	class subMenus:

		def playerInfoDisplay(location, playerData):
			graphics.location.playerInfo(location, playerData)
			gameLocation.showPlayerMenu(location)

		
		def playerCreatureParty(location):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.playerCreatureParty()')
			graphics.location.locationFront(location)
			graphics.creaturePartyDisplay(creatureParty, playerCreature)
			print(' [' + textColor['grn_b'] + 's' + textColor['wht_b'] + '] : Switch Creature')
			print(' [' + textColor['grn_b'] + 'q' + textColor['wht_b'] + '] : Quit')
			graphics.printLine()
			userInput = input('> INPUT: ')
			if userInput == 's': 
				gameLocation.subMenus.switchCreatures(location)
			elif userInput == 'q':
				gameLocation.showPlayerMenu(location)
			else:
				gameLocation.subMenus.playerCreatureParty(location)
			# gameLocation.showPlayerMenu(location)
		
		def playerInventory(location, inventoryHealingItems, inventoryCaptureBalls):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.playerInventory()')
			# graphics.location.locationFront(location)
			dev.clear()
			graphics.printLine()
			graphics.location.playerInventory(inventoryHealingItems, inventoryCaptureBalls)
			userInput = input('> INPUT: ')
			gameLocation.showPlayerMenu(location)
		
		def playerCreatureDex(location, creatureDex):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.playerCreatureDex()')
			player.useCreatureDex(creatureDex, creatureDataList)
			# userInput = input('> INPUT: ')
			gameLocation.showPlayerMenu(location)
		
		def playerMap(location):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.playerMap()')
			map.drawTestMap()
			# userInput = input('\n> INPUT: ')
			gameLocation.showPlayerMenu(location)

		def exploreGoTo(location):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.exploreGoTo()')
			graphics.location.goToStructure(location)

		def exploreTalkTo(location):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.exploreTalkTo()')
			graphics.location.talkToDisplay(location)
		
		def switchCreatures(location):
			dev.debugText('\n> DEBUG: running > gameLocation.subMenus.switchCreatures()')
			global playerCreature
			dev.clear()
			graphics.location.locationFront(location)
			graphics.creaturePartyDisplay(creatureParty, playerCreature)
			print(' > Select a creature to switch')
			userInput = input('\n> INPUT: ')
			err = False
			try:
				targetCreature = creatureParty[int(userInput) - 1]
			except:
				dev.errorText('\n> ERROR: invalid input')
				err = True
			if err == True:
				pass
			else:
				if targetCreature['health'] <= 0:
					print('\n > Cannot switch to fainted creature')
					time.sleep(2)
					gameLocation.subMenus.switchCreatures(location)
				else:
					creature.switchCreatureInParty(targetCreature)
			if userInput == 'q':
				pass
			else:
				gameLocation.subMenus.playerCreatureParty(location)
				

	class npc:

		def talkToNpc(npc, location):
			dev.debugText('\n> DEBUG: running > gameLocation.npc.talkToNpc()')
			graphics.location.npc.npcWindow(npc, location)


# *** //// LOOTING //// ***

class loot:

	def getLoot():
		dev.debugText('\n> DEBUG: running > loot.calculateLoot()')
		randItem = random.randint(0, (globalItemNumber - 1))
		randChance = random.randint(0, 100)
		targetItem = None
		for item in itemDataList:
			if item['id'] == randItem:
				targetItem = item		
		if targetItem['spawnChance'] == 0:
			loot.getLoot()
		else:	
			if targetItem['spawnChance'] >= randChance:
				dev.debugText('\n> DEBUG: found item:')
				dev.debugText('> DEBUG: chance = ' + str(randChance) + '%')
				dev.debugText('> DEBUG: item name = ' + str(targetItem['name']))
				dev.debugText('> DEBUG: spawnChance = ' + str(targetItem['spawnChance']) + '%')
				dev.debugText('> DEBUG: full item = ' + str(targetItem))
				graphics.location.lootFoundDisplay(targetItem)
				inventory.addToInventory(targetItem, 1)
				dev.clear()
				time.sleep(0.1)
			else:
				loot.getLoot()
				
	def startLoot():
		dev.debugText('\n> DEBUG: running > loot.startLoot() ')
		sequence.explore.lootSeq()
		loot.getLoot()	

				
# *** //// CODE EXECUTION //// ***

menu.startUpMenuLoop()

playerData['name'] = 'Lars'
playerData['money'] = 350
playerData['locationID'] = 1

inventory.addToInventory(itemDataList[0], 5)
inventory.addToInventory(itemDataList[1], 5)
inventory.addToInventory(itemDataList[2], 5)
inventory.addToInventory(itemDataList[3], 5)
inventory.addToInventory(itemDataList[4], 5)
inventory.addToInventory(itemDataList[5], 5)
inventory.addToInventory(itemDataList[6], 5)

creature.levelUpCreature(creatureDataList[0], 4)
creature.levelUpCreature(creatureDataList[1], 4)
creature.levelUpCreature(creatureDataList[2], 4)
creature.levelUpCreature(creatureDataList[3], 4)

creature.addCreature(creatureDataList[0])
creature.addCreature(creatureDataList[1])
creature.addCreature(creatureDataList[2])
creature.addCreature(creatureDataList[3])
creature.addCreature(creatureDataList[7])
creature.addCreature(creatureDataList[11])
creature.addCreature(creatureDataList[16])
creature.addCreature(creatureDataList[15])
creature.addCreature(creatureDataList[28])
creature.addCreature(creatureDataList[36])
creature.addCreature(creatureDataList[14])
creature.addCreature(creatureDataList[39])
creature.addCreature(creatureDataList[29])

playerCreature = creatureDataList[0]

gameLocation.mainLocationLoop(locationDataList[1])
gameLocation.mainLocationLoop(locationDataList[2])
testEncounter()
gameLocation.mainLocationLoop(locationDataList[0])
gameLocation.mainLocationLoop(locationDataList[3])

testEncounter()

