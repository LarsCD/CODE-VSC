import tkinter as tk
import random
import time
import os
import pickle
import sys
from operator import itemgetter


from items import *
from player import *
from data import *
from options import *
from debug import *
from graphics import *
from enemies import *


# //////////////// [ GLOBAL ] //////////////// 

thisDir = os.getcwd()

player = playerData
systemData = {
    'settings': systemSettings,
    'options': systemOptions,
    'playerData': playerData,
}









# //////////////// [ SYSTEM ] //////////////// 

class system:

    def startUp():
        debug.log('s', 'SYSTEM STARTUP')

        def startUpPrint():
            version = None
            systemDataSize = sys.getsizeof(systemData)
            cols = systemData['settings']['cmdCols']
            lines = systemData['settings']['cmdLines']

            debug.log('s', 'version         : {}'.format(version))
            debug.log('s', 'resolution      : {}cols, {}lines'.format(cols, lines))
            debug.log('s', 'systemData size : {}b'.format(systemDataSize))

        os.system('color 1') # sets the background to blue (does not work at all on mac you idiot...)
        graphics.importSystemData(systemData)
        cmdCols = systemData['settings']['cmdCols']
        cmdLines = systemData['settings']['cmdCols']
        system.setResolution(cmdCols, cmdLines)
        startUpPrint()
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

        def saveDataPrint(packageData):
            packageDataSize = sys.getsizeof(packageData)
            debug.log('s', 'save nr.      : {}'.format(saveNr))
            debug.log('s', 'loadData size : {}b'.format(packageDataSize))

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
            saveDataPrint(packageData)




    def loadData(saveNr):

        def loadDataPrint(loadedData):
            loadDataSize = sys.getsizeof(loadedData)
            debug.log('s', 'save nr.      : {}'.format(saveNr))
            debug.log('s', 'loadData size : {}b'.format(loadDataSize))

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
            loadDataPrint(loadedData)


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
        debug.log('s', 'set resolution  : {}cols, {}lines'.format(cmdCols, cmdLines))









# //////////////// [ (player) STATS ] //////////////// 

class stats:

    def addXp(quant):
        clr = textColor['cya_b']
        clrStop = textColor[defaultColor]
        print('+ {}{} XP{}'.format(clr, quant, clrStop))
        stats.calculateAddXp(quant)


    def calculateAddXp(quant):
        global player
        xpMax = player['stats']['xpMax']
        if quant >= xpMax:
            quant2 = quant - xpMax 
            stats.levelUp()
            xpMax = player['stats']['xpMax']
            if quant2 >= xpMax:
                stats.calculateAddXp(quant2)
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
        addHpMax = round(100 * (systemData['settings']['globalHpMaxCooficiant'] / 10) + random.randint(2, 7))
        player['stats']['hpMax'] = (oldHpMax + addHpMax)
        oldHp = player['stats']['hp']
        newHp = round(oldHp + addHpMax)
        player['stats']['hp'] = newHp

        # XP MAX ADD
        oldXpMax = player['stats']['xpMax']
        newXpMax = round((player['stats']['xpMax']) * (systemData['settings']['globalXpMaxCooficiant'] / 10))
        player['stats']['xpMax'] = (oldXpMax + newXpMax)

        # EP MAX ADD
        oldEpMax = player['stats']['epMax']
        addEpMax = round(100 * (systemData['settings']['globalEpMaxCooficiant'] / 10) + random.randint(1, 5))
        player['stats']['epMax'] = (oldEpMax + addEpMax)
        oldEp = player['stats']['ep']
        newEp = round(oldEp + addEpMax)
        player['stats']['ep'] = newEp

        # MP MAX ADD 
        oldMpMax = player['stats']['mpMax']
        addMpMax = round(100 * (systemData['settings']['globalMpMaxCooficiant'] / 10) + random.randint(1, 5))
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

        if systemData['options']['debug']['levelUpShow']:
            graphics.clear()
            graphics.ui.playerUI.playerUpStats(player, addHpMax, addEpMax, addMpMax, strUp, spdUp, intUp, gold)
            graphics.click()
        else:
            print('! Player leveled to lvl. {}'.format(player['stats']['level']))
        inventory.addGold(gold)


    def setLevel(level):
        for i in range(level - 1):
            stats.levelUp()













# //////////////// [ PLAYER INVENTORY ] //////////////// 

class inventory:

    def addGold(quant):
        # adds gold to inventory
        global player
        player['inventory']['gold'] += quant
        clr1 = textColor['gol_b']
        stop = textColor[defaultColor]
        print('+ {}{} Gold{} '.format(clr1, quant, stop))
    

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
        itmInInv = inventory.checkItemInInv(targetItem)
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
        inventory.sortInventory(player)


    def removeFromInventory(targetItem, quant):
        # removes item from inventory
        global player
        invType = invTypeKey[targetItem['type']]
        itmInInv = inventory.checkItemInInv(targetItem)
        if itmInInv == True:
            for item in player['inventory'][invType]:
                if item['id'] == targetItem['id']:
                    currentQuantity = item['quantity']
                    newQuantity = int(quant) - currentQuantity
                    targetItem['quantity'] = newQuantity
                    player['inventory'][invType].remove(item)
                    player['inventory'][invType].append(targetItem)
            print('- {} {} '.format(quant, visual.item.display1(targetItem)))
        else:
            pass
        inventory.sortInventory(player)


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


    def sortInventory(player):    # WORKS!! FINALLY (21/4/2021)
        # sets order of items from low to high tier (with fuckin magic...)
        inventory = player['inventory']
        for category in inventory:
            if category == 'gold':
                pass
            else:
                newCategory = sorted(player['inventory'][category], key=itemgetter('tier', 'id')) # Holy grail of the sorting algorithm
                player['inventory'][category] = newCategory
        return player










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









# //////////////// [ PLAYER ] //////////////// 

class playerClass:

    class inventory:

        def useInventory(player): # main function for using inventory
            graphics.clear()
            catIndex = []
            exitInventory = False

            def menu(catIndex):
                userInput = input('\n> ')
                if userInput == '':
                    return False
                if userInput == 'q':
                    return True
                else: 
                    try:
                        userInput = int(userInput)
                    except:
                        pass
                    if isinstance(userInput, int) == True:
                        if int(userInput) < 1 or int(userInput) > len(catIndex):
                            # category does not exist
                            print('\n! You are trying to access a category that doesnt exist...')
                            graphics.click()
                        else: 
                            # GO FURTHER IN CATEGORY 
                            categoryItemList = player['inventory'][catIndex[userInput - 1]]
                            playerClass.inventory.useCategory(categoryItemList)
                            catIndex = []
                    return False

            # FUNCTION START
            while exitInventory == False:
                graphics.clear()
                graphics.line(systemData)
                inventory = player['inventory']
                clr1 = textColor['grn_b']
                stop = textColor[defaultColor]
                print('PLAYER INVENTORY')
                i = 1
                for category in inventory:
                    if category == 'gold':
                        colorStart = textColor['gol_b']
                        colorStop = textColor[defaultColor]
                        print(('\n{}Gold{}: ' + str(inventory['gold']) + '\n').format(colorStart, colorStop))
                    else:
                        itemQuant = len(player['inventory'][category])
                        space = 10 - len(invCatName[category])
                        textSpace = str(' ' * (space))
                        print('[{}{}{}] : {}{}({} items)\n'.format(clr1, (i), stop, invCatName[category], textSpace, itemQuant))
                        i += 1
                        catIndex.append(category)
                print('\n[{}{}{}] : Quit'.format(textColor['grn_b'], 'q', textColor[defaultColor]))
                exitInventory = menu(catIndex) 
                catIndex = []


        def useCategory(itemList): # accesses inventory category (inventory)
            graphics.clear()
            itemIndex = []
            exitCategory = False

            def menu(itemIndex):
                userInput = input('\n> ')
                if userInput == '':
                    pass
                    return False
                if userInput == 'b':
                    return True
                else: 
                    try:
                        # make int if possible
                        userInput = int(userInput)
                    except:
                        pass
                    if isinstance(userInput, int) == True:
                        if int(userInput) > len(itemIndex):
                            pass
                        else:
                            category = invTypeKey[itemList[0]['type']]
                            targerItem = []
                            for item in player['inventory'][category]:
                                if item['id'] == itemIndex[userInput - 1]['id']:
                                    targetItem = item
                            playerClass.inventory.accessItem(targetItem)
                    return False

            # FUNCTION START
            while exitCategory == False:
                try:
                    if itemList == []:
                        graphics.line(systemData)
                        print('PLAYER INVENTORY')
                        print('\n! This category is empty')
                        click = input()
                        break
                    else:
                        category = invTypeKey[itemList[0]['type']]
                    graphics.clear()
                    graphics.line(systemData)
                    inventory = player['inventory']
                    clr1 = textColor['grn_b']
                    stop = textColor[defaultColor]
                    i = 1
                    print(str(invCatName[category]).upper()+'\n')
                    # itemList = []
                    for item in inventory[category]:
                        currentEquip = ''
                        if item == player['loadout']['weapon']:
                            currentEquip = ' - {}Current Weapon{}'.format(clr1, stop)
                        if item == player['loadout']['armor']:
                            currentEquip = ' - {}Current Armor{}'.format(clr1, stop)
                        if item == player['loadout']['shield']:
                            currentEquip = ' - {}Current Shield{}'.format(clr1, stop)
                        else:
                            pass
                        display = graphics.ui.item.itmDisplay1(item)
                        print('[{}{}{}] {} {}x{}'.format(clr1, i, stop, display, str(item['quantity']), currentEquip))
                        i += 1
                        itemIndex.append(item)
                    print('\n[{}{}{}] : Back'.format(textColor['grn_b'], 'b', textColor[defaultColor]))
                    # go in menu and expect bool return (exitCategory)
                    exitCategory = menu(itemIndex)
                except Excepton as e:
                    exitCategory = True
                    break
                    


        def accessItem(targetItem): # access and use target item (inventory)
            graphics.clear()
            exit = False
            global player

            def menu():
                userInput = input('\n> ')
                if userInput == 'b':
                    # # if [b] go back to useInventory
                    return True
                else: 
                    if targetItem['type'] == 'potion':
                        if userInput == 'u':
                            if player['stats']['hp'] == player['stats']['hpMax']:
                                print('\n! Player health is already full')
                                graphics.click()
                            else:
                                print('')
                                playerClass.action.healPlayer(targetItem['healing'])
                                print('')
                                inventory.removeFromInventory(targetItem, 1)
                                graphics.click()
                    elif targetItem['type'] == 'weapon':
                        if userInput == 'e':
                            player['loadout']['weapon'] = targetItem # equip weapon
                            print('\n> Equiped {} as main weapon'.format(graphics.ui.item.itmDisplayShort(targetItem)))
                            graphics.click()
                    elif targetItem['type'] == 'armor':
                        if userInput == 'e':
                            player['loadout']['armor'] = targetItem # equip weapon
                            print('\n> Equiped {} as main armor'.format(graphics.ui.item.itmDisplayShort(targetItem)))
                            graphics.click()
                    elif targetItem['type'] == 'shield':
                        if userInput == 'e':
                            player['loadout']['shield'] = targetItem # equip weapon
                            print('\n> Equiped {} as main shield'.format(graphics.ui.item.itmDisplayShort(targetItem)))
                            graphics.click()
                    elif targetItem['type'] == 'keyItem':
                        pass
                    return False

            while exit == False:
                if targetItem['type'] == 'potion':
                    graphics.ui.inventory.accessPotionDisplay(targetItem)
                elif targetItem['type'] == 'weapon':
                    graphics.ui.inventory.accessWeaponDisplay(targetItem)
                elif targetItem['type'] == 'armor':
                    graphics.ui.inventory.accessArmorDisplay(targetItem)
                elif targetItem['type'] == 'shield':
                    graphics.ui.inventory.accessShieldDisplay(targetItem)
                elif targetItem['type'] == 'keyItem':
                    pass
                exit = menu()


    class action:

        class stats:

            def addXp(quant): # add xp to player
                stats.addXp(quant)


            def healPlayer(heal): # heal player amount of health
                global player
                hp = player['stats']['hp']
                hpMax = player['stats']['hpMax']
                if heal > hpMax - hp:
                    heal = hpMax - hp
                    player['stats']['hp'] = hpMax
                else:
                    player['stats']['hp'] += heal
                hp = player['stats']['hp']
                hpMax = player['stats']['hpMax']
                clr1 = textColor['grn_b']
                stop = textColor[defaultColor]
                if hp < 0.20 * hpMax:
                    clr2 = textColor['red_b']
                    print('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, heal, stop, clr2, hp, stop, clr2, hpMax, stop))
                elif hp < 0.40 * hpMax:
                    clr2 = textColor['org_b']
                    print('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, heal, stop, clr2, hp, stop, clr2, hpMax, stop))
                else:
                    clr2 = textColor['grn_b']
                    print('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, heal, stop, clr2, hp, stop, clr2, hpMax, stop))


        class menu:

            def playerMenu(): # main function for accesing player menu (stats and inventory)
                global player
                exit = False

                def access():
                    userInput = input('\n> ')
                    if userInput == '':
                        return False
                    if userInput == 'q':
                        return True
                    try:
                        # make int if possible
                        userInput = int(userInput)
                    except:
                        pass
                    if isinstance(userInput, int) == True:
                            if userInput == 1:
                                playerClass.info.statsMenu(player)
                            elif userInput == 2:
                                playerClass.inventory.useInventory(player)
                            elif userInput == 3:
                                pass
                            else:
                                pass
                    return False

                while exit == False:
                    graphics.clear()
                    graphics.ui.playerUI.menu.playerMenu()
                    exit = access()


        class loadout:

            def setWeapon(index):  # simple set equiped weapon function
                global player
                player['loadout']['weapon'] = player['inventory']['weapons'][index]

            def setArmor(index):  # simple set equiped armor function
                global player
                player['loadout']['armor'] = player['inventory']['armor'][index]

            def setShield(index):  # simple set equiped shield function
                global player
                player['loadout']['shield'] = player['inventory']['shields'][index]


    class info:

        def statsMenu(player): # main function for player stats
            exit = False

            def menu():
                userInput = input('\n> ')
                if userInput == '':
                    return False
                if userInput == 'q':
                    return True

                return False

            while exit == False:
                graphics.clear()
                graphics.ui.playerUI.playerCurrStats(player)
                print('\n[{}{}{}] : Quit'.format(textColor['grn_b'], 'q', textColor[defaultColor]))
                exit = menu()



            










# //////////////// [ COMBAT ] //////////////// 

class combat:

    def combatLoop(playerIn, enemy): 
        inventory = playerIn['inventory']
        playerStats = playerIn['stats']
        playerLoadout = playerIn['loadout']
        combatOver = False


    def combatMenu(playerIn, enemy): 
        inventory = playerIn['inventory']
        playerStats = playerIn['stats']
        playerLoadout = playerIn['loadout']
        graphics.ui.combat.combatMenu(playerIn, enemy)
        playerInput = input('> ')


    def spellMenu(player): 
        graphics.ui.combat.combatMenuTop(player, enemy)
        print('SPELLBOOK\n')










# //////////////// [ VISUALS ] //////////////// 

class visual:

    class player:
        
        def healthbar():
            display = graphics.ui.playerUI.playerHealthbar(player)
            return display

        def xpBar():
            display = graphics.ui.playerUI.playerXpbar(player)
            return display
        
        def epBar():
            display = graphics.ui.playerUI.playerEpbar(player)
            return display

        def mpBar():
            display = graphics.ui.playerUI.playerMpbar(player)
            return display
        
        def arBar():
            display = graphics.ui.playerUI.playerArBar(player)
            return display
        
        def currentStats():
            graphics.ui.playerUI.playerCurrStats(player)

    class enemy:

        def stats(enemy):
            graphics.ui.enm.enemyStats(enemy)

    class item:

        def display1(targetItem):
            display = graphics.ui.item.itmDisplay1(targetItem)
            return display
    
    class topDisplays:

        def combatMenu(player, enemy):
            graphics.ui.combat.combatMenuTop(player, enemy)












# //////////////// [ CODE EXECUTION ] //////////////// 

system.startUp()
system.saveData(1)

# stats.setLevel(5)
playerClass.action.stats.addXp(50000)

print('')

inventory.addToInventory(itemDataList['potions'][2], 5)
inventory.addToInventory(itemDataList['potions'][3], 5)
inventory.addToInventory(itemDataList['potions'][4], 5)
inventory.addToInventory(itemDataList['potions'][1], 5)
inventory.addToInventory(itemDataList['potions'][0], 5)

print('')
inventory.addToInventory(itemDataList['weapons'][5], 1)
inventory.addToInventory(itemDataList['weapons'][3], 1)
inventory.addToInventory(itemDataList['weapons'][6], 1)
inventory.addToInventory(itemDataList['weapons'][4], 1)
inventory.addToInventory(itemDataList['weapons'][0], 1)
inventory.addToInventory(itemDataList['weapons'][1], 1)
inventory.addToInventory(itemDataList['weapons'][2], 1)

print('')
inventory.addToInventory(itemDataList['armor'][0], 1)
inventory.addToInventory(itemDataList['armor'][4], 1)
inventory.addToInventory(itemDataList['armor'][1], 1)
inventory.addToInventory(itemDataList['armor'][2], 1)
inventory.addToInventory(itemDataList['armor'][3], 1)

print('')
inventory.addToInventory(itemDataList['shields'][0], 1)
inventory.addToInventory(itemDataList['shields'][1], 1)
inventory.addToInventory(itemDataList['shields'][2], 1)
inventory.addToInventory(itemDataList['shields'][3], 1)
inventory.addToInventory(itemDataList['shields'][4], 1)
print('')
inventory.addToInventory(itemDataList['spells'][0], 1)
inventory.addToInventory(itemDataList['spells'][1], 1)
inventory.addToInventory(itemDataList['spells'][2], 1)
inventory.addToInventory(itemDataList['spells'][3], 1)
inventory.addToInventory(itemDataList['spells'][4], 1)
inventory.addToInventory(itemDataList['spells'][5], 1)
inventory.addToInventory(itemDataList['spells'][6], 1)
inventory.addToInventory(itemDataList['spells'][7], 1)
inventory.addToInventory(itemDataList['spells'][8], 1)
print('')
inventory.addGold(1150)
print('')
stats.addXp(43)
print('')

playerClass.action.loadout.setWeapon(0)
playerClass.action.loadout.setArmor(0)
playerClass.action.loadout.setShield(0)

# system.saveData(1)

print('\n'*4)


# playerClass.action.menu.playerMenu()
system.loadData(1)
graphics.click()
inventory.addToInventory(itemDataList['weapons'][0], 1)
inventory.addToInventory(itemDataList['weapons'][1], 1)
graphics.click()
inventory.addToInventory(itemDataList['potions'][0], 5)
inventory.addToInventory(itemDataList['potions'][1], 5)
graphics.click()
# playerClass.action.menu.playerMenu()


enemy1 = enemyDataList[0]
enemy1 = enemy.levelSet(enemy1, 40)
playerClass.action.menu.playerMenu()
# print('\n'*1)
battleStats.playerAttack(player)
print('')
battleStats.enemyAttack(enemy1)
print('\n'*2)
visual.enemy.stats(enemy1)
print('\n'*2)
combat.combatMenu(player, enemy1)
graphics.ui.combat.combatMessage1(enemy1)
graphics.ui.combat.combatMenu(player, enemy1)

