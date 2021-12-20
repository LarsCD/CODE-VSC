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
