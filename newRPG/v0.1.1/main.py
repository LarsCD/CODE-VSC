import tkinter as tk
import random
import time
import os
import pickle

from items import *
from player import *
from data import *
from debug import *
from graphics import *
from enemies import *
from spells import *



# //////////////// [ GLOBAL ] //////////////// 

thisDir = os.getcwd()

player = playerData
systemData = {
    'settings': settings, 
    'playerData': playerData,
}



# //////////////// [ SYSTEM ] //////////////// 

class system:

    def startUp():
        cmdCols = systemData['settings']['cmdCols']
        cmdLines = systemData['settings']['cmdCols']
        system.setResolution(cmdCols, cmdLines)
        debug.log('s', 'SYSTEM STARTUP')
        system.createDir('saves')
        print('')


    def initColors():
        colorInitColor = textColor[defaultColor]
        print(colorInitColor)
    

    def initSystemData():
        global player
        player = systemData['playerData']
    

    def packageData():
        global systemData
        systemData['playerData'] = player


    def saveData(saveNr):
        debug.log('s', ('[!!] saving system data...'))
        system.packageData()
        packageData = systemData
        targetSave = ('save{}'.format(str(saveNr)))
        try:
            saveDataDirPath = os.path.join('saves', targetSave)
            saveDataPath = os.path.join(thisDir, saveDataDirPath)
            file = open(saveDataPath, 'wb')
        except FileNotFoundError:
            debug.log('e', ('no file to save data to'))
        else: 
            pickle.dump(packageData, file)
            file.close()
            debug.log('s', ('{} successfully saved').format(targetSave))


    def loadData(saveNr):
        global systemData
        debug.log('s', ('[!!] loading system data...'))
        targetSave = ('save{}'.format(str(saveNr)))
        try:
            saveDataDirPath = os.path.join('saves', targetSave)
            saveDataPath = os.path.join(thisDir, saveDataDirPath)
            file = open(saveDataPath, 'rb')
        except FileNotFoundError:
            debug.log('e', ('no file to load data from'))
        else: 
            loadedData = pickle.load(file)
            file.close()
            systemData = loadedData
            system.initSystemData()
            debug.log('s', ('{} successfully loaded').format(targetSave))


    def createDir(dirName): 
        debug.log('s', ('adding subdir \'' + dirName + '\' to current dir'))
        path = os.path.join(thisDir, dirName)
        try:  
            os.mkdir(path)
        except IsADirectoryError: 
            debug.log('e', ('could not create dir \'' + dirName + '\', dir already exists'))
        except Exception as e: 
            debug.log('e', ('could not create dir \'' + dirName + '\''))
            debug.log('e', (str(e)))
    
    def setResolution(cmdCols, cmdLines):
        os.system('mode con cols={} lines={}'.format(cmdCols, cmdLines))



# //////////////// [ PLAYER STATS ] //////////////// 

class playerStat:

    def addXp(quant):
        clr = textColor['cya_b']
        clrStop = textColor[defaultColor]
        print('+ {}{} XP{}'.format(clr, quant, clrStop))
        playerStat.calculateAddXp(quant)


    def calculateAddXp(quant):
        global player
        xpMax = player['stats']['xpMax']
        if quant >= xpMax:
            quant2 = quant - xpMax 
            playerStat.levelUp()
            xpMax = player['stats']['xpMax']
            if quant2 >= xpMax:
                playerStat.calculateAddXp(quant2)
            else:
                player['stats']['xp'] = quant2
        else: 
            player['stats']['xp'] = quant


    def levelUp():
        # up stats for level up
        global player  
        player['stats']['level'] += 1

        # HP MAX ADD
        oldHpMax = player['stats']['hpMax']
        addHpMax = round(100 * (settings['globalHpMaxCooficiant']/10) + random.randint(2, 7))
        player['stats']['hpMax'] = (oldHpMax + addHpMax)
        oldHp = player['stats']['hp']
        newHp = round(oldHp + addHpMax)
        player['stats']['hp'] = newHp

        # XP MAX ADD
        oldXpMax = player['stats']['xpMax']
        newXpMax = round((player['stats']['xpMax'])*(settings['globalXpMaxCooficiant']/10))
        player['stats']['xpMax'] = (oldXpMax + newXpMax)

        # EP MAX ADD
        oldEpMax = player['stats']['epMax']
        addEpMax = round(100 * (settings['globalEpMaxCooficiant']/10) + random.randint(1, 5))
        player['stats']['epMax'] = (oldEpMax + addEpMax)
        oldEp = player['stats']['ep']
        newEp = round(oldEp + addEpMax)
        player['stats']['ep'] = newEp

        # MP MAX ADD 
        oldMpMax = player['stats']['mpMax']
        addMpMax = round(100 * (settings['globalMpMaxCooficiant']/10) + random.randint(1, 5))
        player['stats']['mpMax'] = (oldMpMax + addMpMax)
        oldMp = player['stats']['mp']
        newMp = round(oldMp + addMpMax)
        player['stats']['mp'] = newMp

        # STR ADD
        strUp = random.randint(1, 2)
        oldStr = player['stats']['str']
        player['stats']['str'] = (oldStr + strUp)

        # SPD ADD
        spdUp = random.randint(1, 2)
        oldSpd = player['stats']['spd']
        player['stats']['spd'] = (oldSpd + spdUp)

        # INT ADD
        intUp = random.randint(1, 2)
        oldInt = player['stats']['int']
        player['stats']['int'] = (oldInt + intUp)
        
        gold = (player['stats']['level'] * 50)
        graphics.ui.plr.playerUpStats(player, addHpMax, addEpMax, addMpMax, strUp, spdUp, intUp, gold)
        playerInv.addGold(gold)


    def setLevel(level):
        for i in range(level - 1):
            playerStat.levelUp()



# //////////////// [ PLAYER INVENTORY ] //////////////// 

class playerInv:

    def addGold(quant):
        # adds gold to inventory
        global player
        player['inventory']['gold'] += quant
        colorStart = textColor['gol_b']
        colorStop = textColor[defaultColor]
        print('+ {} {}Gold{} '.format(quant, colorStart, colorStop))
    

    def subGold(quant):
        # subtracts gold from inventory
        global player
        if (player['inventory']['gold'] - quant) < 0:
            actualQuant = quant - player['inventory']['gold']
            print('! cannot subtract more gold then is in inventory')
            player['inventory']['gold'] = 0
            colorStart = textColor['gol_b']
            colorStop = textColor[defaultColor]
            print('- {} {}Gold{} '.format(actualQuant, colorStart, colorStop))
        else:
            player['inventory']['gold'] -= quant
            colorStart = textColor['gol_b']
            colorStop = textColor[defaultColor]
            print('- {} {}Gold{} '.format(quant, colorStart, colorStop))


    def addToInventory(targetItem, quant):
        # adds item to inventory
        global player
        invType = invTypeKey[targetItem['type']]
        itmInInv = playerInv.checkItemInInv(targetItem)
        if itmInInv == True:
            if targetItem['stackable'] == True:
                for item in player['inventory'][invType]:
                    if item['id'] == targetItem['id']:
                        currentQuantity = item['quantity']
                        newQuantity = int(quant) + currentQuantity
                        targetItem['quantity'] = newQuantity
                        debug.log('d', player['inventory'][invType])
                        debug.log('d', targetItem)
                        player['inventory'][invType].remove(item)
                        player['inventory'][invType].append(targetItem)
                print('+ {} {} '.format(quant, visual.item.display1(targetItem)))
            else:
                print('! cannot add {} because item is not stackable'.format(visual.item.display1(targetItem)))
        else: 
            if targetItem['stackable'] == True:
                targetItem['quantity'] = quant
                player['inventory'][invType].append(targetItem)
                print('+ {} {} '.format(quant, visual.item.display1(targetItem)))
            else:
                targetItem['quantity'] = 1
                player['inventory'][invType].append(targetItem)
                print('+ 1 {} '.format(visual.item.display1(targetItem)))
        # playerInv.sortInventory()


    def removeFromInventory(targetItem, quant):
        # removes item from inventory
        global player
        invType = invTypeKey[targetItem['type']]
        itmInInv = playerInv.checkItemInInv(targetItem)
        if itmInInv == True:
            for item in player['inventory'][invType]:
                if item['id'] == targetItem['id']:
                    currentQuantity = item['quantity']
                    newQuantity = int(quant) + currentQuantity
                    item['quantity'] = newQuantity
                    player['inventory'][invType].remove(targetItem)
                    player['inventory'][invType].append(item)
            print('- {} {} '.format(quant, visual.item.display1(targetItem)))
        else:
            pass


    def addSpell(targetSpell):
        global player
        spells = player['spells']
        spllInInv = playerInv.checkSpellInInv(targetSpell)
        spllDisplay = graphics.ui.spell.spllDisplay1(targetSpell)
        if spllInInv == False:
            if len(spells) <= player['stats']['spellsMax']:
                spells.append(targetSpell)
                player['spells'] = spells
                print('+ {}'.format(spllDisplay))
            else:
                print('! {} cannot be added, max amount spells'.format(spllDisplay))
                # debug.log('d', '{} cannot be added, max amount spells'.format(spllDisplay))



    def checkItemInInv(targetItem):
        # checks if item in inventory, returns true/false
        inventory = player['inventory']
        targetItemID = targetItem['id']
        returnValue = False
        for category in inventory:
            if category == 'gold':
                pass
            else:
                for item in inventory[category]:
                    if targetItemID == item['id']:
                        returnValue = True
                        break
        return returnValue


    def checkSpellInInv(targetSpell):
        # checks if spell in inventory, returns true/false
        spells = player['spells']
        targetSpellID = targetSpell['id']
        returnValue = False
        for spell in spells:
            if targetSpellID == spell['id']:
                returnValue = True
                break
        return returnValue
    

    def sortInventory():    # DOESNT WORK ATM  (plz fix future lars)
        # sets order of items from low to high index (with magic...)
        global player
        for invType in player['inventory']:
            if invType == 'gold':
                pass
            else:
                targetInventory = player['inventory'][invType]
                sortKey = lambda targetInventory: targetInventory['id']
                newTargetInventory = targetInventory.sort(key=sortKey)
                player['inventory'][invType] = newTargetInventory
                # this is one shitshow... Doenst work, not using it atm



# //////////////// [ ENEMY ] //////////////// 

class enemy: 

    def levelSet(enemy, level):
        for i in range(level - 1):
            enemy['stats']['level'] += 1
            baseHp = enemy['stats']['baseHp']
            hpAdd = round((baseHp * 0.5) + enemy['stats']['lvlRange'])
            enemy['stats']['hpMax'] += hpAdd
            enemy['stats']['hp'] = enemy['stats']['hpMax']
            enemy['stats']['str'] += random.randint(1, 2)
            enemy['stats']['spd'] += random.randint(1, 2)
        return enemy



# //////////////// [ BATTLE STATS ] //////////////// 

class battleStats: 

    def playerAttack(player):
        stats = player['stats']
        weapon = player['loadout']['weapon']
        baseAttack = 0
        clr = textColor['red_b']
        stop = textColor[defaultColor]
        if weapon['type'] == 'weapon':
            baseAttack = (round(stats['level'] * 1.0) + stats['str'])
            debug.log('d', 'player baseAttack = {}'.format(baseAttack))
            addAttack = random.randint(weapon['damage'][0], weapon['damage'][1])
            debug.log('d', 'player addAttack = {}'.format(addAttack))
            expAttack = weapon['tier']
            debug.log('d', 'player expAttack = {}'.format(expAttack))
            attackDmg = ((baseAttack * expAttack) + addAttack)
            print('Player attack damage: {}{}{} dmg'.format(clr, attackDmg, stop))
            return attackDmg


    def enemyAttack(enemy):
        stats = enemy['stats']
        weapon = enemy['loadout']['weapon']
        baseAttack = 0
        clr = textColor['red_b']
        stop = textColor[defaultColor]
        if weapon['type'] == 'weapon':
            baseAttack = (round(stats['level'] * 1.0) + stats['str'])
            debug.log('d', 'enemy baseAttack = {}'.format(baseAttack))
            addAttack = random.randint(weapon['damage'][0], weapon['damage'][1])
            debug.log('d', 'enemy addAttack = {}'.format(addAttack))
            expAttack = weapon['tier']
            debug.log('d', 'enemy expAttack = {}'.format(expAttack))
            attackDmg = ((baseAttack * expAttack) + addAttack)
            print('Enemy attack damage: {}{}{} dmg'.format(clr, attackDmg, stop))
            return attackDmg


# //////////////// [ COMBAT ] //////////////// 

class combat:

    def combatLoop(playerIn, enemy): 
        playerInv = playerIn['inventory']
        playerStats = playerIn['stats']
        playerLoadout = playerIn['loadout']
        combatOver = False


    def combatMenu(playerIn, enemy): 
        playerInv = playerIn['inventory']
        playerStats = playerIn['stats']
        playerLoadout = playerIn['loadout']
        graphics.ui.combat.combatMenu(playerIn, enemy)



# //////////////// [ VISUALS ] //////////////// 

class visual:

    class player:

        def inventory_n():
            graphics.ui.inv.printInv(player)
        
        def healthbar():
            display = graphics.ui.plr.playerHealthbar(player)
            return display

        def xpBar():
            display = graphics.ui.plr.playerXpbar(player)
            return display
        
        def epBar():
            display = graphics.ui.plr.playerEpbar(player)
            return display

        def mpBar():
            display = graphics.ui.plr.playerMpbar(player)
            return display
        
        def arBar():
            display = graphics.ui.plr.playerArBar(player)
            return display
        
        def currentStats():
            graphics.ui.plr.playerCurrStats(player)

    class enemy:

        def stats(enemy):
            graphics.ui.enm.enemyStats(enemy)

    class item:

        def display1(targetItem):
            display = graphics.ui.item.itmDisplay1(targetItem)
            return display



# //////////////// [ CODE EXECUTION ] //////////////// 

system.startUp()
system.saveData(1)
playerStat.setLevel(40)
print('')
playerInv.addToInventory(itemDataList['potions'][0], 3)
playerInv.addToInventory(itemDataList['potions'][1], 3)
playerInv.addToInventory(itemDataList['potions'][2], 3)
playerInv.addToInventory(itemDataList['potions'][3], 3)
playerInv.addToInventory(itemDataList['potions'][4], 3)
print('')
playerInv.addToInventory(itemDataList['weapons'][0], 1)
playerInv.addToInventory(itemDataList['weapons'][1], 1)
playerInv.addToInventory(itemDataList['weapons'][2], 1)
playerInv.addToInventory(itemDataList['weapons'][3], 1)
playerInv.addToInventory(itemDataList['weapons'][4], 1)
print('')
playerInv.addToInventory(itemDataList['armor'][0], 1)
playerInv.addToInventory(itemDataList['armor'][1], 1)
playerInv.addToInventory(itemDataList['armor'][2], 1)
playerInv.addToInventory(itemDataList['armor'][3], 1)
playerInv.addToInventory(itemDataList['armor'][4], 1)
print('')
playerInv.addToInventory(itemDataList['shields'][0], 1)
playerInv.addToInventory(itemDataList['shields'][1], 1)
playerInv.addToInventory(itemDataList['shields'][2], 1)
playerInv.addToInventory(itemDataList['shields'][3], 1)
playerInv.addToInventory(itemDataList['shields'][4], 1)
print('')
playerInv.addSpell(spellDataList[0])
playerInv.addSpell(spellDataList[1])
playerInv.addSpell(spellDataList[2])
playerInv.addSpell(spellDataList[3])
playerInv.addSpell(spellDataList[4])
playerInv.addSpell(spellDataList[5])
playerInv.addSpell(spellDataList[6])
playerInv.addSpell(spellDataList[7])
playerInv.addSpell(spellDataList[8])
print('')
playerInv.addGold(1150)
print('')
playerStat.addXp(43)
print('')
player['loadout']['weapon'] = player['inventory']['weapons'][4]
player['loadout']['armor'] = player['inventory']['armor'][4]
player['loadout']['shield'] = player['inventory']['shields'][4]

# enemy1 = enemy.levelUp(enemyDataList['basic'][0], 5)
enemy1 = enemyDataList[0]
enemy1 = enemy.levelSet(enemy1, 40)

visual.player.currentStats()
# visual.player.inventory_n()
# print('\n'*1)

battleStats.playerAttack(player)
print('')
battleStats.enemyAttack(enemy1)

# print('\n'*2)
# visual.enemy.stats(enemy1)

# print('\n'*2)

combat.combatMenu(player, enemy1)

# graphics.ui.combat.combatMessage1(enemy1)
# graphics.ui.combat.combatMenu(player, enemy1)

# graphics.clear()

# print('\n'*50)
# visual.player.currentStats()
# visual.player.inventory_n()
# system.loadData(1)
# visual.player.currentStats()
# visual.player.inventory_n()