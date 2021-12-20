# import tkinter as tk
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
from newRpg_saveReader import *


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
        global enemyGlobalData
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

        enemyGlobalData = system.initEnemyData(enemyDataList)

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

        return loadedData


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

    def initEnemyData(enemyDataList_IN) -> object:
        globalDataLable = {'globalDataID': 1}
        enemyDataList = 0
        enemyGlobalData = enemyDataList_IN.copy()
        return enemyGlobalData









# //////////////// [ DATA MANAGEMENT ] ////////////////

class Data:

    class Item_data(*args):
        pass








# //////////////// [ (PLAYER) STATS ] ////////////////

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

    def subEp(epCost):
        global player
        player['stats']['ep'] -= epCost


    def subMp(mpCost):
        global player
        player['stats']['mp'] -= mpCost


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
        itemIninventory = inventory.checkItemInInv(targetItem)
        if itemIninventory == True:
            if targetItem['stackable'] == True:
                for item in player['inventory'][invType]:
                    if item['id'] == targetItem['id']:
                        currentQuantity = item['quantity']
                        newQuantity = int(quant) + currentQuantity
                        targetItem['quantity'] = newQuantity
                        player['inventory'][invType].remove(item)
                        player['inventory'][invType].append(targetItem)
                print('+ {} {} '.format(quant, visual.item.display1(targetItem)))
            else:
                print('! cannot add {} because item is not stackable'.format(visual.item.displayShort(targetItem)))
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

    def sortInventory(player):  # WORKS!! FINALLY (21/4/2021)
        # sets order of items from low to high tier (with fuckin magic...)
        inventory = player['inventory']
        for category in inventory:
            if category == 'gold':
                pass
            else:
                newCategory = sorted(player['inventory'][category],
                                     key=itemgetter('tier', 'id'))  # Holy grail of the sorting algorithm
                player['inventory'][category] = newCategory
        return player

















# //////////////// [ GAME CLASS ] ////////////////

class gameClass:

    def givePlayerAllItems(itemDataList):
        for cat in itemDataList:
            for item in itemDataList[cat]:
                inventory.addToInventory(item, 1)

















# //////////////// [ PLAYER CLASS ] ////////////////

class playerClass:

    class inventory:

        def useInventory(player): # main function for using inventory
            graphics.clear()
            catIndex = []
            exitInventory = False

            def menu(catIndex):
                userInput = input('\n> ')
                if userInput == '':
                    return False, 0
                if userInput == 'q':
                    return True, 0
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
                            choice = playerClass.inventory.useCategory(categoryItemList)
                            if choice != 0:
                                return True, choice
                            catIndex = []
                    return False, 0

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
                exitInventory, choice = menu(catIndex)
                if choice != 0:
                    break
                catIndex = []
            return choice


        def useCategory(itemList): # accesses inventory category (inventory)
            graphics.clear()
            itemIndex = []
            exitCategory = False

            def menu(itemIndex):
                userInput = input('\n> ')
                if userInput == '':
                    pass
                    return False, 0
                if userInput == 'b':
                    return True, 0
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
                            choice = playerClass.inventory.accessItem(targetItem)
                            if choice != 0:
                                return True, choice
                    return False, 0

            # FUNCTION START
            while exitCategory == False:
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
                exitCategory, choice = menu(itemIndex)


            return choice
                    


        def accessItem(targetItem): # access and use target item (inventory)
            graphics.clear()
            exit = False
            global player

            def menu():
                userInput = input('\n> ')
                if userInput == 'b':
                    # # if [b] go back to useInventory
                    return True, 0
                else: 
                    if targetItem['type'] == 'potion':
                        if userInput == 'u':
                            if player['stats']['hp'] == player['stats']['hpMax']:
                                print('\n! Player health is already full')
                                graphics.click()
                            else:
                                if player['data']['isInCombat'] == True:
                                    return True, targetItem
                                else:
                                    print('')
                                    playerClass.action.stats.healPlayer(targetItem['healing'])
                                    print('')
                                    inventory.removeFromInventory(targetItem, 1)
                                    graphics.click()
                                    return True, 0
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
                            print('\n> Equiped {} as mainshield'.format(graphics.ui.item.itmDisplayShort(targetItem)))
                            graphics.click()
                    elif targetItem['type'] == 'keyItem':
                        pass
                    elif targetItem['type'] == 'spell':
                        if userInput == 'c': # cast spell
                            return True, targetItem

                    return False, 0

            while exit == False:
                if targetItem['type'] == 'potion':
                    graphics.ui.inventory.accessPotionDisplay(targetItem)
                elif targetItem['type'] == 'weapon':
                    graphics.ui.inventory.accessWeaponDisplay(targetItem)
                elif targetItem['type'] == 'armor':
                    graphics.ui.inventory.accessArmorDisplay(targetItem)
                elif targetItem['type'] == 'shield':
                    graphics.ui.inventory.accessShieldDisplay(targetItem)
                elif targetItem['type'] == 'spell':
                    graphics.ui.inventory.accessSpellDisplay(targetItem)
                elif targetItem['type'] == 'keyItem':
                    pass
                exit, choice = menu()
            return choice



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
                message = ''
                if hp < 0.20 * hpMax:
                    clr2 = textColor['red_b']
                    message = ('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, heal, stop, clr2, hp, stop, clr2, hpMax, stop))
                elif hp < 0.40 * hpMax:
                    clr2 = textColor['org_b']
                    message = ('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, heal, stop, clr2, hp, stop, clr2, hpMax, stop))
                else:
                    clr2 = textColor['grn_b']
                    message = ('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, heal, stop, clr2, hp, stop, clr2, hpMax, stop))
                if player['data']['isInCombat'] == False:
                    print(message)

            def damagePlayer(playerIn, damage):
                playerIn['stats']['hp'] -= damage
                if playerIn['stats']['hp'] < 0:
                    playerIn['stats']['hp'] = 0
                return playerIn



            def damageLoadoutArmor(playerIn, damage):
                if  playerIn['loadout']['armor'] == None:
                    pass
                else:
                    playerIn['loadout']['armor']['hp'] -= damage
                    if playerIn['loadout']['armor']['hp'] < 0:
                        playerIn['loadout']['armor']['hp'] = 0
                        playerIn['loadout']['armor']['isBroken'] = True
                return playerIn


            def damageLoadoutShield(playerIn, damage):
                if  playerIn['loadout']['shield'] == None:
                    pass
                else:
                    playerIn['loadout']['shield']['hp'] -= damage
                    if playerIn['loadout']['shield']['hp'] < 0:
                        playerIn['loadout']['shield']['hp'] = 0
                        playerIn['loadout']['shield']['isBroken'] = True
                return playerIn


        class menu:

            def playerMenu(): # main function for accesing player menu (stats and inventory)
                global player
                exit = False

                def access():
                    userInput = input('\n> ')
                    if userInput == '':
                        return False, 0
                    if userInput == 'q':
                        return True, 0
                    try:
                        # make int if possible
                        userInput = int(userInput)
                    except:
                        pass
                    if isinstance(userInput, int) == True:
                            if userInput == 1:
                                playerClass.info.statsMenu(player)
                            elif userInput == 2:
                                choice = playerClass.inventory.useInventory(player)
                                if choice != 0:
                                    return True, choice
                            else:
                                pass
                    return False, 0

                while exit == False:
                    graphics.clear()
                    graphics.ui.playerUI.menu.playerMenu(player)
                    exit, choice = access()
                    if choice != 0:
                        return choice
                    else:
                        return 0


            def spellOnlyMenu(player): # re-used useCatagory func from inventory
                categoryItemList = player['inventory']['spells']
                inventoryChoice = playerClass.inventory.useCategory(categoryItemList)
                return inventoryChoice
                    
                    
            def gameMenu():
                exit = False
                
                def saveGameMessage():
                    choice = False
                    while choice == False:
                        graphics.clear()
                        graphics.line(systemData)
                        print('CONFIRM')
                        print('\nConfirm Save:\n')
                        print('[{}{}{}]  : Yes'.format(textColor['grn_b'], 'y', textColor[defaultColor]))
                        print('[{}{}{}]  : No\n'.format(textColor['grn_b'], 'enter', textColor[defaultColor]))                        
                        playerInput = input('> ')
                        if playerInput == 'y':
                            print('')
                            system.saveData(1)
                            graphics.click()
                            break
                        else: 
                            break
                            
                def loadGameMessage():
                    choice = False
                    while choice == False:
                        graphics.clear()
                        graphics.line(systemData)
                        print('CONFIRM')
                        print('\nConfirm Load:\n')
                        print('[{}{}{}]      : Yes'.format(textColor['grn_b'], 'y', textColor[defaultColor]))
                        print('[{}{}{}]  : No\n'.format(textColor['grn_b'], 'enter', textColor[defaultColor]))                        
                        playerInput = input('> ')
                        if playerInput == 'y':
                            print('')
                            system.loadData(1)
                            graphics.click()
                            break
                        else: 
                            break
                        
                
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
                                saveGameMessage()
                            elif userInput == 2:
                                loadGameMessage()
                            elif userInput == 3:
                                pass
                            else:
                                pass

                    return False
                while exit == False:
                    graphics.clear()
                    graphics.ui.playerUI.menu.gameMenu()
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


    def initPlayerData(playerIn):
        global player
        player = playerIn











# //////////////// [ ENEMY CLASS ] ////////////////

class enemyClass:


    def createEnemyEntity(id, level, enemyGlobalData_IN) -> object:
        enemyGlobalData_COPY = enemyGlobalData_IN.copy()
        enemyData = enemyGlobalData_COPY
        enemyData = enemyClass.levelSet(enemyData, level)
        return enemyData



    def levelSet(enemy, level) -> object:
        for i in range(level - 1):
            enemy['stats']['level'] += 1
            baseHp = enemy['stats']['baseHp']
            hpAdd = round((baseHp * 0.5) + enemy['stats']['lvlRange'])
            enemy['stats']['hpMax'] += hpAdd
            enemy['stats']['hp'] = enemy['stats']['hpMax']
            enemy['stats']['str'] += random.randint(1, 2)
            enemy['stats']['spd'] += random.randint(1, 2)
        return enemy


    def enemyAIChoice(enemy, player):
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)
        choice = 0
        # choice: 1 = attack, 2 = block, 3 = heal
        if rand1 <= ((1 / enemy['stats']['level']) * 100):
            # immediat attack (no matter low hp)
            choice = 1
        else:
            if enemy['stats']['hp'] <= (enemy['stats']['hp'] * 0.25) and rand1 >= 50:
                # if low health and high percentage (50%)
                if player['stats']['hp'] <= (player['stats']['hp'] * 0.25) and rand2 >= 20:
                    # attack if player is also low
                    choice = 1
                else:
                    # otherwise heal
                    choice = 3
            elif enemy['stats']['hp'] <= (enemy['stats']['hp'] * 0.60) and rand2 >= 20:
                # if medium health and low percentage (20%)
                if enemy['loadout']['shield'] != None:
                    # if enemy has shield
                    if player['stats']['hp'] <= (player['stats']['hp'] * 0.25) and rand2 >= 20:
                        # if player health low, attack
                        choice = 1
                    else:
                        # otherwise block
                        choice = 2
                else:
                    # if no shield, attack
                    choice = 1
            else:
                # if enemy health not low, attack
                choice = 1

        return choice


    class stats:

        def healEnemy(enemy, heal):
            hp = enemy['stats']['hp']
            hpMax = enemy['stats']['hpMax']
            if heal > hpMax - hp:
                heal = hpMax - hp
                enemy['stats']['hp'] = hpMax
            else:
                enemy['stats']['hp'] += heal
            return enemy

        def damageEnemy(enemy, damage):
            enemy['stats']['hp'] -= damage
            if enemy['stats']['hp'] < 0:
                enemy['stats']['hp'] = 0
            return enemy



        def damageLoadoutArmor(enemy, damage):
            if enemy['loadout']['armor'] == None:
                pass
            else:
                enemy['loadout']['armor']['hp'] -= damage
                if enemy['loadout']['armor']['hp'] < 0:
                    enemy['loadout']['armor']['hp'] = 0
                    enemy['loadout']['armor']['isBroken'] = True
            return enemy



        def damageLoadoutShield(enemy, damage):
            if enemy['loadout']['shield'] == None:
                pass
            else:
                enemy['loadout']['shield']['hp'] -= damage
                if enemy['loadout']['shield']['hp'] < 0:
                    enemy['loadout']['shield']['hp'] = 0
                    enemy['loadout']['shield']['isBroken'] = True
            return enemy


















# //////////////// [ BATTLE STATS ] ////////////////

class battleStats:

    def calcPlayerWeaponAttack(playerIn):
        stats = playerIn['stats']
        weapon = playerIn['loadout']['weapon']
        baseAttack = 0
        clr = textColor['red_b']
        stop = textColor[defaultColor]
        crit = False
        rand = random.randint(1, 100)
        if (weapon['critChance'] * 100) >= rand:
            crit = True

        if weapon['type'] == 'weapon':
            baseAttack = random.randint(weapon['damage'][0], weapon['damage'][1])
            # debug.log('d', 'player baseAttack = {}'.format(baseAttack))
            addAttack = stats['str']
            # debug.log('d', 'player addAttack = {}'.format(addAttack))
            if crit == True:
                debug.log('d', 'player: CRIT!')
                attackDmg = round((baseAttack + addAttack) * 2)
            else:
                attackDmg = round(baseAttack + addAttack)
            debug.log('d', 'player attack attackDmg: {}{}{} dmg'.format(clr, attackDmg, stop))
            return attackDmg



    def calcPlayerSpellAttack(playerIn, spell):
        stats = playerIn['stats']
        baseAttack = 0
        clr = textColor['red_b']
        stop = textColor[defaultColor]
        crit = False
        rand = random.randint(1, 100)
        if (spell['critChance'] * 100) >= rand:
            crit = True
        if spell['spellType'] == 'damage':
            baseAttack = random.randint(spell['damage'][0], spell['damage'][1])
            # debug.log('d', 'player baseAttack = {}'.format(baseAttack))
            addAttack = stats['int']
            # debug.log('d', 'player addAttack = {}'.format(addAttack))
            if crit == True:
                attackDmg = round((baseAttack + addAttack) * 2)
            else:
                attackDmg = round(baseAttack + addAttack)
            debug.log('d', 'player spell attackDmg: {}{}{} dmg'.format(clr, attackDmg, stop))
            return attackDmg



    def calcPlayerDamage(playerIn, attackDamage, choice):
        blockDmgShield = 0
        blockDmgArmor = 0
        shield = playerIn['loadout']['shield']
        armor = playerIn['loadout']['armor']
        if shield != None and playerIn['loadout']['shield']['isBroken'] == False and choice == 2:
            blockDmgShield = round(attackDamage * shield['disperse'])
        if armor != None and playerIn['loadout']['armor']['isBroken'] == False:
            blockDmgArmor = round((attackDamage - blockDmgShield) * armor['disperse'])
        playerDmg = attackDamage - blockDmgShield - blockDmgArmor
        return blockDmgShield, blockDmgArmor, playerDmg



    def calcEnemyWeaponAttack(enemy):
        stats = enemy['stats']
        weapon = enemy['loadout']['weapon']
        baseAttack = 0
        clr = textColor['red_b']
        stop = textColor[defaultColor]
        crit = False
        rand = random.randint(1, 100)
        if (weapon['critChance'] * 100) >= rand:
            crit = True
        if weapon['type'] == 'weapon':
            baseAttack = random.randint(weapon['damage'][0], weapon['damage'][1])
            # debug.log('d', 'enemy baseAttack = {}'.format(baseAttack))
            addAttack = stats['str']
            # debug.log('d', 'enemy addAttack = {}'.format(addAttack))
            if crit == True:
                debug.log('d', 'enemy: CRIT!')
                attackDmg = round((baseAttack + addAttack) * 2)
            else:
                attackDmg = round(baseAttack + addAttack)
            debug.log('d', 'enemy weapon attack attackDmg: {}{}{} dmg'.format(clr, attackDmg, stop))
            return attackDmg



    def calcEnemyDamage(enemy, attackDamage, choice):
        blockDmgShield = 0
        blockDmgArmor = 0
        shield = enemy['loadout']['shield']
        armor = enemy['loadout']['armor']
        if shield != None and enemy['loadout']['shield']['isBroken'] == False and choice == 2:
            blockDmgShield = round(attackDamage * shield['disperse'])
        if armor != None and enemy['loadout']['armor']['isBroken'] == False:
            blockDmgArmor = round((attackDamage - blockDmgShield) * armor['disperse'])
        enemyDmg = attackDamage - blockDmgShield - blockDmgArmor
        return blockDmgShield, blockDmgArmor, enemyDmg










# //////////////// [ COMBAT ] //////////////// 

class combat:

    def combatMenu(playerIn, enemy): # main function for combat interaction
        debug.log('d', 'combatMenu')

        exit = False

        def access():
            userInput = input('\n> ')
            if userInput == '':
                return False, 0, 0
            if userInput == 'q':
                return True, 0, 0
            try:
                # make int if possible
                userInput = int(userInput)
            except:
                pass
            if isinstance(userInput, int) == True:
                    if userInput == 1:
                        # WEAPON (ATTACK) [1]
                        if playerIn['loadout']['weapon']['epCost'] > playerIn['stats']['ep']:
                            print('\n! EP too low to attack')
                            graphics.click()
                            return False, 0, 0
                        else:
                            return True, 1, player['loadout']['weapon']
                    elif userInput == 2:
                        # SHIELD (BLOCK) [2]
                        if player['loadout']['shield'] == None:
                            print('\n! No Shield equiped')
                            graphics.click()
                            return False, 0, 0
                        elif player['loadout']['shield']['isBroken']:
                            print('\n! Equiped Shield is broken')
                            graphics.click()
                            return False, 0, 0
                        elif playerIn['loadout']['shield']['epCost'] > playerIn['stats']['ep']:
                            print('\n! EP too low to block')
                            graphics.click()
                        else:
                            return True, 2, player['loadout']['shield']
                    elif userInput == 3:
                        # SPELL (ATK, DEF, HEAL) [3]
                        inventoryChoice = playerClass.action.menu.spellOnlyMenu(playerIn)
                        if inventoryChoice != 0:
                            if inventoryChoice['mpCost'] > playerIn['stats']['mp']:
                                print('\n! MP too low to cast Spell')
                                graphics.click()
                                return False, 0, 0
                            return True, 3, inventoryChoice
                        else:
                            return False, 3, 0
                    elif userInput == 4:
                        # INVETORY (COULD BE SPELL OR POTION) [4]
                        inventoryChoice = playerClass.action.menu.playerMenu()
                        if inventoryChoice != 0:
                            return True, 4, inventoryChoice
                        else:
                            return False, 4, 0
                    elif userInput == 5:
                        # run from enemy (RUN AWAY AYY...) [5]
                        return True, 5, 0
            return False, 0, 0

        while exit == False:
            graphics.clear()
            graphics.ui.combat.combatMenu(playerIn, enemy)
            exit, choice, inventoryChoice = access()

        debug.log('d', 'combatMenu END')
        return choice, inventoryChoice



    def combatLoop(playerIn, enemyIn):
        debug.log('d', 'combatLoop')
        inCombat = True
        combatOver = False
        playerIn['data']['isInCombat'] = inCombat

        playerClass.initPlayerData(playerIn)
        graphics.ui.combat.combatMessage1(enemyIn)


        def calculateCombatState(playerIn, enemyIn):
            playerWon = False
            combatOver = False
            if enemyIn['stats']['hp'] == 0:
                playerWon = True
                combatOver = True
            elif playerIn['stats']['hp'] == 0:
                playerWon = False
                combatOver = True
            else:
                combatOver = False
            return playerWon, combatOver


        while combatOver == False:
            # BEGIN COMBAT ROUND
            # MAIN COMBAT ROUND FUNCTIONS
            # debug.log('d', 'ROUND BEGIN')
            choice, inventoryChoice = combat.combatMenu(playerIn, enemyIn)

            if choice == 5:
                # RUN
                combat.playerRunsAway(playerIn, enemyIn)
                combatOver = True
                break
            else:
                playerCombatData, enemyCombatData = combat.calculateCombat(playerIn, enemyIn, choice, inventoryChoice)
                playerIn, enemyIn = combat.executeCombatRound(playerIn, enemyIn, playerCombatData, enemyCombatData)
                playerWon, combatOver = calculateCombatState(playerIn, enemyIn)
                if playerWon == True:
                    # PLAYER WINS
                    combat.playerWins(playerIn, enemyIn)
                elif combatOver == True:
                    # PLAYER LOSES (DIES)
                    pass



        debug.log('d', 'combatLoop END')

    def playerRunsAway(playerIn, enemy):
        graphics.clear()
        graphics.line(systemData)
        clr0 = textColor['red_b']
        stop = textColor[defaultColor]
        print('You ran away from {}{}{}'.format(clr0, enemy['general']['name'], stop))
        graphics.click()
        inCombat = False
        player['data']['isInCombat'] = False

    def playerWins(playerIn, enemy):
        graphics.clear()
        graphics.line(systemData)
        enemyLevel = enemy['stats']['level']
        print('{}{}{} defeted {}{}{}')
        stats.addXp((enemyLevel * 25) + ((enemyLevel - playerIn['stats']['level']) * 2))
        graphics.click()




    def calculateCombat(playerIn, enemy, playerChoice, inventoryChoice):
        debug.log('d', 'calculateCombat')
        # PLAYER

        playerCombatData = {
            'playerChoice': 0,
            'playerAttack': 0,
            'playerShieldBlock': 0,
            'playerArmorBlock': 0,
            'playerHeal': 0,
            'playerDamage': 0,
            'goesFirst': False,
            'usedItem': None,
        }

        playerCombatData['playerChoice'] = playerChoice
        usedItem = None
        # PLAYER: ITEM (POTION) USE
        if playerChoice == 4:
            if inventoryChoice['type'] == 'potion':
                playerCombatData['playerHeal'] = inventoryChoice['healing']
                playerCombatData['usedItem'] = inventoryChoice
            elif inventoryChoice['type'] == 'spell':
                playerChoice = 3

        # PLAYER: ATTACK / SPELL CAST
        if playerChoice == 1 or playerChoice == 3: # ATTACK / SPELL
            if playerChoice == 1: # ATTACK WEAPON
                playerCombatData['playerAttack'] = battleStats.calcPlayerWeaponAttack(playerIn)
            else: # ATTACKSPELL
                playerCombatData['usedItem'] = inventoryChoice
                if inventoryChoice['spellType'] == 'damage':
                    playerCombatData['playerAttack'] = battleStats.calcPlayerSpellAttack(playerIn, inventoryChoice)
                elif inventoryChoice['spellType'] == 'healing':
                    playerCombatData['playerHeal'] = inventoryChoice[inventoryChoice['spellType']]

        # ENEMY
        enemyChoice = enemyClass.enemyAIChoice(enemy, playerIn)
        enemyCombatData = {
            'enemyChoice': 0,
            'enemyAttack': 0,
            'enemyShieldBlock': 0,
            'enemyArmorBlock': 0,
            'enemyHeal': 0,
            'enemyDamage': 0,
            'goesFirst': False,
        }

        enemyCombatData['enemyChoice'] = enemyChoice
        if enemyChoice == 3:
            enemyCombatData['enemyHeal'] = enemy['stats']['healFactor'] * enemy['stats']['hpMax']
        elif enemyChoice == 1:
            enemyCombatData['enemyAttack'] = battleStats.calcEnemyWeaponAttack(enemy)

        # CALCULATE ORDER (who goes first)
        if playerChoice == 4:
            if enemyChoice == 3:
                playerCombatData['goesFirst'] = True
            else:
                enemyCombatData['goesFirst'] = True
        elif playerChoice == 2:
            if enemyChoice == 3:
                enemyCombatData['goesFirst'] = True
            elif enemyChoice == 2:
                playerCombatData['goesFirst'] = True
            elif enemyChoice == 1:
                enemyCombatData['goesFirst'] = True
        else:
            if enemyChoice == 3:
                enemyCombatData['goesFirst'] = True
            elif enemyChoice == 2:
                playerCombatData['goesFirst'] = True
            elif enemyChoice == 1:
                if playerIn['stats']['spd'] >= enemy['stats']['spd']:
                    playerCombatData['goesFirst'] = True
                else:
                    enemyCombatData['goesFirst'] = True


        # PLAYER FINAL DATA
        playerCombatData['playerShieldBlock'], playerCombatData['playerArmorBlock'], playerCombatData['playerDamage'] = battleStats.calcPlayerDamage(playerIn, enemyCombatData['enemyAttack'], playerChoice)

        # ENEMY FINAL DATA
        enemyCombatData['enemyShieldBlock'], enemyCombatData['enemyArmorBlock'], enemyCombatData['enemyDamage'] = battleStats.calcEnemyDamage(enemy, playerCombatData['playerAttack'], enemyChoice)

        print('\n')
        debug.log('d', 'calculateCombat END')
        return playerCombatData, enemyCombatData



    def executeCombatRound(playerIn, enemy, playerCombatData, enemyCombatData):
        # NOTE: This function is a 350 line mess
        # NOTE: I gave up, it should work, if it doenst good luck...
        graphics.clear()
        graphics.ui.combat.combatMenuTopShort(playerIn, enemy)
        graphics.line(systemData)
        print('COMBAT\n')

        def playerCombatExecution(playerIn):
            clr0 = textColor['grn_b']
            clr1 = textColor['red_b']
            clr2 = textColor['ylw_b']
            clr3 = textColor['blu_2']
            clr4 = textColor['blu_b']
            stop = textColor[defaultColor]

            shieldBlock = playerCombatData['playerShieldBlock']
            playerChoice = playerCombatData['playerChoice']
            actionUsed = False

            if playerChoice == 4:
                if playerCombatData['usedItem']['type'] == 'potion':
                    actionUsed = True
                    # PLAYER USES POTION
                    playerHpMax = playerIn['stats']['hpMax']
                    heal = playerCombatData['playerHeal']
                    playerHp = playerIn['stats']['hp'] + heal
                    if playerHp > playerHpMax:
                        playerHp = playerHpMax
                    playerClass.action.stats.healPlayer(heal)
                    print('> {}{}{} uses {}'.format(clr0, playerIn['general']['name'], stop, visual.item.displayShort(playerCombatData['usedItem'])))
                    if playerHp < 0.20 * playerHpMax:
                        clr2 = textColor['red_b']
                        message = ('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr0, heal, stop, clr2, playerHp, stop, clr2, playerHpMax, stop))
                    elif playerHp < 0.40 * playerHpMax:
                        clr2 = textColor['org_b']
                        message = ('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr0, heal, stop, clr2, playerHp, stop, clr2, playerHpMax, stop))
                    else:
                        clr2 = textColor['grn_b']
                        message = ('+ {}{}{} HP  ({}{}{}/{}{}{})'.format(clr0, heal, stop, clr2, playerHp, stop, clr2, playerHpMax, stop))
                    print(message)
                else:
                    playerChoice == 3
                    # # PLAYER ATTACKS WITH SPELL
                    # actionUsed = True
                    # mpCost = playerCombatData['usedItem']['mpCost']
                    # mpCostMessage = '- {}{}{} MP'.format(clr4, mpCost, stop)
                    # stats.subMp(mpCost)
                    # if playerCombatData['goesFirst'] == True:
                    #     combatFirstMessage = [' attacks first!', ' is ahead of the enemy!', ' starts the attack!',' charges into battle!']
                    #     print('> {}{}{}{}'.format(clr0, playerIn['general']['name'], stop,combatFirstMessage[random.randint(0, 3)]))
                    #     graphics.click()
                    # print('> {}{}{} casts {}'.format(clr0, playerIn['general']['name'], stop,visual.item.displayShort(playerCombatData['usedItem'])))
                    # graphics.click()
                    # print('> {}{}{} deals {}{}{} dmg  ({})'.format(clr0, playerIn['general']['name'], stop, clr1,playerCombatData['playerAttack'], stop,mpCostMessage))
                    # graphics.click()

            elif playerChoice == 3:
                # PLAYER USES SPELL
                if playerCombatData['usedItem']['spellType'] == 'damage':
                    # PLAYER ATTACKS WITH SPELL
                    actionUsed = True
                    mpCost = playerCombatData['usedItem']['mpCost']
                    mpCostMessage = '- {}{}{} MP'.format(clr4, mpCost, stop)
                    stats.subMp(mpCost)
                    if playerCombatData['goesFirst'] == True:
                        combatFirstMessage = [' attacks first!', ' is ahead of the enemy!', ' starts the attack!',' charges into battle!']
                        print('> {}{}{}{}'.format(clr0, playerIn['general']['name'], stop,combatFirstMessage[random.randint(0, 3)]))
                        graphics.click()
                    print('> {}{}{} casts {}'.format(clr0, playerIn['general']['name'], stop,visual.item.displayShort(playerCombatData['usedItem'])))
                    graphics.click()
                    print('> {}{}{} deals {}{}{} dmg  ({})'.format(clr0, playerIn['general']['name'], stop, clr1,playerCombatData['playerAttack'], stop, mpCostMessage))
                    graphics.click()

                elif playerCombatData['usedItem']['spellType'] == 'block':
                    print('\nplayer casts {}'.format(visual.item.displayShort(playerCombatData['usedItem'])))
                    graphics.click()
                elif playerCombatData['usedItem']['spellType'] == 'healing':
                    print('\nplayer casts {}'.format(visual.item.displayShort(playerCombatData['usedItem'])))
                    graphics.click()

            elif playerChoice == 1:
                # PLAYER ATTACKS
                epCost = player['loadout']['weapon']['epCost']
                epCostMessage = '-{}{}{} EP'.format(clr2, epCost, stop)
                stats.subEp(epCost)

                if playerCombatData['goesFirst'] == True:
                    combatFirstMessage = [' attacks first!', ' is ahead of the enemy!', ' starts the attack!', ' charges into battle!']
                    print('> {}{}{}{}'.format(clr0, playerIn['general']['name'], stop, combatFirstMessage[random.randint(0, 3)]))
                    graphics.click()
                print('> {}{}{} attacks with {}'.format(clr0, playerIn['general']['name'], stop, visual.item.displayShort(playerIn['loadout']['weapon'])))
                graphics.click()
                print('> {}{}{} deals {}{}{} dmg  ({})'.format(clr0, playerIn['general']['name'], stop, clr1, playerCombatData['playerAttack'], stop, epCostMessage))
                graphics.click()

            playerClass.initPlayerData(playerIn)
            return playerIn


        def playerCombatExecutionDamage(playerIn):
            clr0 = textColor['grn_b']
            clr1 = textColor['red_b']
            clr2 = textColor['ylw_b']
            clr3 = textColor['blu_2']
            clr4 = textColor['blu_b']
            stop = textColor[defaultColor]

            armorBlock = playerCombatData['playerArmorBlock']
            playerDamage = playerCombatData['playerDamage']
            shieldBlock = playerCombatData['playerShieldBlock']

            playerIn = playerClass.action.stats.damagePlayer(playerIn, playerDamage)
            playerChoice = playerCombatData['playerChoice']

            if playerChoice == 2:
                if shieldBlock > 0:
                    epCost = player['loadout']['shield']['epCost']
                    stats.subEp(epCost)
                    epCostMessage = '-{}{}{} EP'.format(clr2, epCost, stop)
                    playerIn = playerClass.action.stats.damageLoadoutShield(playerIn, shieldBlock)
                    print('> {}{}{} blocks attack with {}'.format(clr0, playerIn['general']['name'], stop, visual.item.displayShort(playerIn['loadout']['shield'])))
                    graphics.click()
                    print('> {}{}{} shield blocks {}{}{} dmg  ({})'.format(clr0, playerIn['general']['name'], stop, clr3,shieldBlock, stop, epCostMessage))
                    graphics.click()
            if armorBlock > 0:
                playerIn = playerClass.action.stats.damageLoadoutArmor(playerIn, armorBlock)
                print('> {}{}{} armor blocks {}{}{} dmg  '.format(clr0, playerIn['general']['name'], stop, clr3, armorBlock, stop))
                graphics.click()
            print('> {}{}{} takes {}{}{} dmg'.format(clr0, playerIn['general']['name'], stop, clr1, playerDamage, stop))
            graphics.click()
            playerClass.initPlayerData(playerIn)
            return playerIn



        def enemyCombatExecution(enemy):
            clr0 = textColor['grn_b']
            clr1 = textColor['red_b']
            clr2 = textColor['ylw_b']
            clr3 = textColor['blu_2']
            clr4 = textColor['blu_b']
            stop = textColor[defaultColor]

            shieldBlock = playerCombatData['playerShieldBlock']
            enemyChoice = enemyCombatData['enemyChoice']

            if enemyChoice == 3:
                # PLAYER USES POTION
                enemyHpMax = enemy['stats']['hpMax']
                heal = enemyCombatData['enemyHeal']
                enemyHp = enemy['stats']['hp'] + heal
                enemy = enemyClass.stats.healEnemy(enemy, heal)
                if enemyHp > enemyHpMax:
                    enemyHp = enemyHpMax
                print('> {}{}{} is healing'.format(clr0, enemy['general']['name'], stop,))
                if enemyHp < 0.20 * enemyHpMax:
                    clr2 = textColor['red_b']
                    message = ('+ {}{}{} {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, enemy['general']['name'], stop, clr0, heal, stop, clr2, enemyHp, stop, clr2, enemyHpMax,stop))
                elif enemyHp < 0.40 * enemyHpMax:
                    clr2 = textColor['org_b']
                    message = ('+ {}{}{} {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, enemy['general']['name'], stop, clr0, heal, stop, clr2, enemyHp, stop, clr2, enemyHpMax,stop))
                else:
                    clr2 = textColor['grn_b']
                    message = ( '+ {}{}{} {}{}{} HP  ({}{}{}/{}{}{})'.format(clr1, enemy['general']['name'], stop, clr0, heal, stop, clr2, enemyHp, stop, clr2, enemyHpMax,stop))
                print(message)

            elif enemyChoice == 1:
                if enemyCombatData['goesFirst'] == True:
                    combatFirstMessage = [' attacks first!', ' is ahead of you!', ' starts the attack!',' charges into battle!']
                    print('> {}{}{}{}'.format(clr1, enemy['general']['name'], stop,combatFirstMessage[random.randint(0, 3)]))
                    graphics.click()
                print('> {}{}{} attacks and deals {}{}{} dmg '.format(clr1, enemy['general']['name'], stop, clr1, enemyCombatData['enemyAttack'], stop))
                graphics.click()

            return enemy


        def enemyCombatExecutionDamage(enemy):
            clr0 = textColor['grn_b']
            clr1 = textColor['red_b']
            clr2 = textColor['ylw_b']
            clr3 = textColor['blu_2']
            clr4 = textColor['blu_b']
            stop = textColor[defaultColor]

            enemyDamage = enemyCombatData['enemyDamage']
            armorBlock = enemyCombatData['enemyArmorBlock']
            shieldBlock = playerCombatData['playerShieldBlock']
            enemy = enemyClass.stats.damageEnemy(enemy, enemyDamage)
            enemyChoice = enemyCombatData['enemyChoice']

            if enemyChoice == 2:
                enemy = enemyClass.stats.damageLoadoutShield(enemy, shieldBlock)
                print('> {}{}{} shield blocks {}{}{} dmg  '.format(clr1, enemy['general']['name'], stop, clr3, shieldBlock, stop))
                graphics.click()
            if armorBlock > 0:
                enemy = enemyClass.stats.damageLoadoutArmor(enemy, armorBlock)
                print('\n> {}{}{} armor blocks {}{}{} dmg  '.format(clr1, enemy['general']['name'], stop, clr3, armorBlock, stop))
                graphics.click()
            print('> {}{}{} takes {}{}{} dmg'.format(clr1, enemy['general']['name'], stop, clr1, enemyDamage, stop))
            graphics.click()
            return enemy


        # COMBAT EXECUTION
        if playerCombatData['goesFirst'] == True:
            # PLAYER GOES FIRST
            playerIn = playerCombatExecution(playerIn)
            enemy = enemyCombatExecutionDamage(enemy) # SHADY SHIT HAPPENS HERE (NOTE: fixed, i was dumb...)
            enemy = enemyCombatExecution(enemy)
            playerIn = playerCombatExecutionDamage(playerIn)

        else:
            # ENEMY GOES FIRST
            enemy = enemyCombatExecution(enemy)
            playerIn = playerCombatExecutionDamage(playerIn)
            playerIn = playerCombatExecution(playerIn)
            enemy = enemyCombatExecutionDamage(enemy)

        try:
            if enemy['data'] != None:
                debug.log('e', 'end of combat execution: IMPOSTOR SPOTED!!!!')
        except:
            pass
        return playerIn, enemy

















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
            graphics.ui.enemyUI.enemyStats(enemy)

    class item:

        def display1(targetItem):
            display = graphics.ui.item.itmDisplay1(targetItem)
            return display

        def displayShort(targetItem):
            display = graphics.ui.item.itmDisplayShort(targetItem)
            return display
    
    class topDisplays:

        def combatMenu(player, enemy):
            graphics.ui.combat.combatMenuTop(player, enemy)












# //////////////// [ CODE EXECUTION ] ////////////////

if __name__ == '__main__':
    system.startUp()



    # gameClass.givePlayerAllItems(itemDataList)
    #
    # playerClass.action.loadout.setWeapon(7)
    # playerClass.action.loadout.setArmor(2)
    # playerClass.action.loadout.setShield(2)


    # playerClass.action.menu.playerMenu()


    # playerClass.action.menu.gameMenu()
    # saveReader.readSaveFile(1)



    # enemyGlobalData = enemyDataList[1]
    # print(enemyGlobalData)
    # enemy1 = enemyClass.createEnemyEntity(1, 10, enemyGlobalData)
    # enemy2 = enemyClass.createEnemyEntity(1, 15, enemyGlobalData)
    #
    # combat.combatLoop(player, enemy1)
    #
    # combat.combatLoop(player, enemy2)




