import time
import os
import random
from data import *


class graphics: 


    def line():
        print('-' * round(settings['cmdCols']))

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
        # os.system('clear')
        pass
    
    def click():
        input()


    class ui: 

        class general:

            def customBar(text, min, max, len, char, color):
                colorStart = color
                colorStop = textColor[defaultColor]

                disp1 = (str(text) + ": (" + colorStart + str(min) + colorStop + "/" + colorStart + str(max) + colorStop + ")" + colorStop)
                percentageBar = round((min / max) * 100)
                barNum = round(len*(percentageBar/100))
                disp2 = ("[" + (str(colorStart + (str(char)) + colorStop) * barNum + ("." * round(len-barNum)) + "]"))
                display = (disp1 + " " + disp2)
                return display


        class playerUI:

            def playerHealthbar(player):
                hp = player['stats']['hp']
                hpMax = player['stats']['hpMax']
                fullBar = 30 # length healthbar chars
                text = 'HEALTH '
                char = '■'
                if hp < 0.20 * hpMax:
                    colorStart = textColor['red_b']
                    colorStop = textColor[defaultColor]
                elif hp < 0.40 * hpMax:
                    colorStart = textColor['org_b']
                    colorStop = textColor[defaultColor]
                else:
                    colorStart = textColor['grn_b']
                    colorStop = textColor[defaultColor]

                disp1 = (str(text) + ": (" + colorStart + str(hp) + colorStop + "/" + colorStart + str(hpMax) + colorStop + ")" + colorStop)
                percentageBar = round((hp / hpMax) * 100)
                barNum = round(fullBar*(percentageBar/100))
                disp2 = ("[" + (str(colorStart + (char) + colorStop) * barNum + ("." * round(fullBar-barNum)) + "]"))
                display = (disp1 + " " + disp2)
                return display


            def playerXpbar(player):
                min = player['stats']['xp']
                max = player['stats']['xpMax']
                len = 30 # length healthbar chars
                text = 'XP     '
                char = '■'
                colorStart = textColor['cya_b']
                colorStop = textColor[defaultColor]

                disp1 = (str(text) + ": (" + colorStart + str(min) + colorStop + "/" + colorStart + str(max) + colorStop + ")" + colorStop)
                percentageBar = round((min / max) * 100)
                barNum = round(len*(percentageBar/100))
                disp2 = ("[" + (str(colorStart + (str(char)) + colorStop) * barNum + ("." * round(len-barNum)) + "]"))
                display = (disp1 + " " + disp2)
                return display
            

            def playerEpbar(player):
                min = player['stats']['ep']
                max = player['stats']['epMax']
                len = 30 # length healthbar chars
                text = 'ENERGY '
                char = '»'
                colorStart = textColor['ylw_b']
                colorStop = textColor[defaultColor]

                disp1 = (str(text) + ": (" + colorStart + str(min) + colorStop + "/" + colorStart + str(max) + colorStop + ")" + colorStop)
                percentageBar = round((min / max) * 100)
                barNum = round(len*(percentageBar/100))
                disp2 = ("[" + (str(colorStart + (str(char)) + colorStop) * barNum + ("." * round(len-barNum)) + "]"))
                display = (disp1 + " " + disp2)
                return display
            

            def playerMpbar(player):
                min = player['stats']['mp']
                max = player['stats']['mpMax']
                len = 30 # length healthbar chars
                text = 'MANA   '
                char = '»'
                colorStart = textColor['blu_b']
                colorStop = textColor[defaultColor]

                disp1 = (str(text) + ": (" + colorStart + str(min) + colorStop + "/" + colorStart + str(max) + colorStop + ")" + colorStop)
                percentageBar = round((min / max) * 100)
                barNum = round(len*(percentageBar/100))
                disp2 = ("[" + (str(colorStart + (str(char)) + colorStop) * barNum + ("." * round(len-barNum)) + "]"))
                display = (disp1 + " " + disp2)
                return display
            
            def playerArBar(player):
                colorStart = textColor['blu_2']
                colorStop = textColor[defaultColor]
                if player['loadout']['armor'] == None:
                    display = 'ARMOR  : ({}0{}/{}0{})   [....................]'.format(colorStart, colorStop, colorStart, colorStop)
                else:
                    min = player['loadout']['armor']['hp']
                    max = player['loadout']['armor']['hpMax']
                    len = 20 # length healthbar chars
                    text = 'ARMOR  '
                    char = '×'
                    colorStart = textColor['blu_2']
                    colorStop = textColor[defaultColor]

                    disp1 = (str(text) + ": (" + colorStart + str(min) + colorStop + "/" + colorStart + str(max) + colorStop + ")" + colorStop)
                    percentageBar = round((min / max) * 100)
                    barNum = round(len*(percentageBar/100))
                    disp2 = ("[" + (str(colorStart + (str(char)) + colorStop) * barNum + ("." * round(len-barNum)) + "]"))
                    display = (disp1 + " " + disp2)
                    return display
                return display
            

            def playerShBar(player):
                colorStart = textColor['red_b']
                colorStop = textColor[defaultColor]
                if player['loadout']['shield'] == None:
                    display = 'SHIELD : ({}0{}/{}0{})   [....................]'.format(colorStart, colorStop, colorStart, colorStop)
                else:
                    min = player['loadout']['shield']['hp']
                    max = player['loadout']['shield']['hpMax']
                    len = 20 # length healthbar chars
                    text = 'SHIELD '
                    char = '×'
                    colorStart = textColor['red_b']
                    colorStop = textColor[defaultColor]

                    disp1 = (str(text) + ": (" + colorStart + str(min) + colorStop + "/" + colorStart + str(max) + colorStop + ")" + colorStop)
                    percentageBar = round((min / max) * 100)
                    barNum = round(len*(percentageBar/100))
                    disp2 = ("[" + (str(colorStart + (str(char)) + colorStop) * barNum + ("." * round(len-barNum)) + "]"))
                    display = (disp1 + " " + disp2)
                    return display
                return display

            

            def playerCurrStats(player):
                colorStart1 = textColor['ylw_b']
                colorStart2 = textColor['blu_b']
                colorStop = textColor[defaultColor]
                graphics.line()
                print('PLAYER STATS\n')
                print('Name       : {}'.format(player['general']['name']))
                print('Level      : {}'.format(player['stats']['level']))
                print('Character  : {}\n'.format(player['general']['character']))
                print(graphics.ui.playerUI.playerHealthbar(player))
                print(graphics.ui.playerUI.playerArBar(player))
                print(graphics.ui.playerUI.playerShBar(player))
                print('')
                print(graphics.ui.playerUI.playerEpbar(player))
                print(graphics.ui.playerUI.playerMpbar(player))
                print(graphics.ui.playerUI.playerXpbar(player))
                print('\nLoadout:')
                weapon = graphics.ui.item.itmDisplay1(player['loadout']['weapon']) 
                armor = graphics.ui.item.itmDisplay1(player['loadout']['armor']) 
                shield = graphics.ui.item.itmDisplay1(player['loadout']['shield']) 
                print('- Weapon   : {}'.format(weapon))
                print('- Armor    : {}'.format(armor))
                print('- Shield   : {}'.format(shield))
                print('\nStrength : {}'.format(player['stats']['str']))
                print('Speed    : {}'.format(player['stats']['spd']))
                print('Intel.   : {}'.format(player['stats']['int']))
                # graphics.line()


            def playerUpStats(player, hpUp, epUp, mpUp, strUp, spdUp, intUp, gold):
                clr1 = textColor['grn_b']
                clr2 = textColor['ylw_b']
                clr3 = textColor['blu_b']
                lenHp = (4-len(str(hpUp)))
                lenEp = (4-len(str(epUp)))
                lenMp = (4-len(str(mpUp)))
                clrStop = textColor[defaultColor]
                graphics.line()
                print('LEVEL UP!\n')
                print('Lvl : {}'.format(player['stats']['level']))
                print('\nHP  : +{}{}{}  (Max: {}{}{})'.format(clr1, hpUp, clrStop, clr1, player['stats']['hpMax'], clrStop))
                print('EP  : +{}{}{}  (Max: {}{}{})'.format(clr2, epUp, clrStop, clr2, player['stats']['epMax'], clrStop))
                print('MP  : +{}{}{}  (Max: {}{}{})\n'.format(clr3, mpUp, clrStop, clr3, player['stats']['mpMax'], clrStop))
                print('Str : +{}'.format(strUp))
                print('Spd : +{}'.format(spdUp))
                print('Int : +{}'.format(intUp))
                if gold > 0:
                    clr1 = textColor['gol_b']
                    stop = textColor[defaultColor]
                    print('+ {}{} Gold{} '.format(clr1, gold, stop))
                graphics.line()


            class menu:

                def playerMenu():
                    graphics.line()
                    print('PLAYER MENU\n')
                    print('[{}{}{}] : Stats'.format(textColor['grn_b'], '1', textColor[defaultColor]))
                    print('\n[{}{}{}] : Inventory'.format(textColor['grn_b'], '2', textColor[defaultColor]))

                    print('\n\n[{}{}{}] : Quit'.format(textColor['grn_b'], 'q', textColor[defaultColor]))



        class inventory:

            def accessPotionDisplay(targetItem):
                graphics.clear()
                name = graphics.ui.item.itmDisplay1(targetItem)
                itemType = (targetItem['type']).capitalize()
                value = targetItem['value']
                stackBool = targetItem['stackable']
                quantity = targetItem['quantity']

                healing = targetItem['healing']

                stackable = ''
                if stackBool == True:
                    stackable = 'Yes'
                else:
                    stackable = 'No'

                clr1 = textColor[itmTierColor[targetItem['tier']]]
                clr2 = textColor['ylw_b']
                clr3 = textColor['grn_b']
                stop = textColor[defaultColor]

                graphics.line()
                print(name+' - ({}x)\n'.format(targetItem['quantity']))
                print('Healing      : {}{}{} HP'.format(clr3, healing, stop))
                print('\nValue        : {}{}{} gold'.format(clr2, value, stop))
                print('Type         : {}'.format(itemType))
                print('Stackable    : {}'.format(stackable))
                print('Quantity    : {}'.format(quantity))
                print('\n[{}{}{}] : Use'.format(textColor['grn_b'], 'u', textColor[defaultColor]))
                print('[{}{}{}] : Back'.format(textColor['grn_b'], 'b', textColor[defaultColor]))

            
            def accessWeaponDisplay(targetItem):
                graphics.clear()
                name = graphics.ui.item.itmDisplay1(targetItem)
                itemType = (targetItem['type']).capitalize()
                value = targetItem['value']
                stackBool = targetItem['stackable']

                avgDamage = round((targetItem['damage'][0] + targetItem['damage'][1]) / 2)
                epCost = targetItem['epCost']
                critChance = round(targetItem['critChance'] * 100)

                stackable = ''
                if stackBool == True:
                    stackable = 'Yes'
                else:
                    stackable = 'No'

                clr1 = textColor[itmTierColor[targetItem['tier']]]
                clr2 = textColor['ylw_b']
                clr3 = textColor['red_b']
                clr4 = textColor['ylw_b']
                stop = textColor[defaultColor]

                graphics.line()
                print(name+'\n')
                print('Avg. Attack  : {}{}{} ATK'.format(clr3, avgDamage, stop))
                print('Energy Cost  : {}{}{} EP'.format(clr4, epCost, stop))
                print('Crit chance  : {}%'.format(critChance))
                print('\nValue        : {}{}{} gold'.format(clr2, value, stop))
                print('Type         : {}'.format(itemType))
                print('Stackable    : {}'.format(stackable))
                print('\n[{}{}{}] : Equip'.format(textColor['grn_b'], 'e', textColor[defaultColor]))
                print('[{}{}{}] : Back'.format(textColor['grn_b'], 'b', textColor[defaultColor]))
            

            def accessArmorDisplay(targetItem):
                graphics.clear()
                name = graphics.ui.item.itmDisplay1(targetItem)
                itemType = (targetItem['type']).capitalize()
                value = targetItem['value']
                stackBool = targetItem['stackable']

                armorHp = targetItem['hp']
                armorHpMax = targetItem['hpMax']
                disperse = round(targetItem['disperse'] * 100, 1)

                isBroken = ''
                if targetItem['isBroken'] == True:
                    isBroken = 'Yes'
                else:
                    isBroken = 'No'

                stackable = ''
                if stackBool == True:
                    stackable = 'Yes'
                else:
                    stackable = 'No'

                clr1 = textColor[itmTierColor[targetItem['tier']]]
                clr2 = textColor['ylw_b']
                clr3 = None
                clr4 = textColor['ylw_b']
                stop = textColor[defaultColor]

                if armorHp < 0.20 * armorHpMax:
                    clr3 = textColor['red_b']
                elif armorHp < 0.40 * armorHpMax:
                    clr3 = textColor['org_b']
                else:
                    clr3 = textColor['grn_b']

                graphics.line()
                print(name+'\n')
                print('Armor HP      : {}{}{} HP'.format(clr3, armorHp, stop))
                print('Armor max HP  : {} max HP'.format(armorHpMax))
                print('Disperse      : {}%'.format(disperse))
                print('\nValue          : {}{}{} gold'.format(clr2, value, stop))
                print('Type          : {}'.format(itemType))
                print('Stackable     : {}'.format(stackable))
                print('Is Broken     : {}'.format(isBroken))
                print('\n[{}{}{}] : Equip'.format(textColor['grn_b'], 'e', textColor[defaultColor]))
                print('[{}{}{}] : Back'.format(textColor['grn_b'], 'b', textColor[defaultColor]))
            
            
            def accessShieldDisplay(targetItem):
                graphics.clear()
                name = graphics.ui.item.itmDisplay1(targetItem)
                itemType = (targetItem['type']).capitalize()
                value = targetItem['value']
                stackBool = targetItem['stackable']

                shieldHp = targetItem['hp']
                shieldHpMax = targetItem['hpMax']
                disperse = round(targetItem['disperse'] * 100, 1)

                isBroken = ''
                if targetItem['isBroken'] == True:
                    isBroken = 'Yes'
                else:
                    isBroken = 'No'

                stackable = ''
                if stackBool == True:
                    stackable = 'Yes'
                else:
                    stackable = 'No'

                clr1 = textColor[itmTierColor[targetItem['tier']]]
                clr2 = textColor['ylw_b']
                clr3 = None
                clr4 = textColor['ylw_b']
                stop = textColor[defaultColor]

                if shieldHp < 0.20 * shieldHpMax:
                    clr3 = textColor['red_b']
                elif shieldHp < 0.40 * shieldHpMax:
                    clr3 = textColor['org_b']
                else:
                    clr3 = textColor['grn_b']

                graphics.line()
                print(name+'\n')
                print('Armor HP      : {}{}{} HP'.format(clr3, shieldHp, stop))
                print('Armor max HP  : {} max HP'.format(shieldHpMax))
                print('Disperse      : {}%'.format(disperse))
                print('\nValue          : {}{}{} gold'.format(clr2, value, stop))
                print('Type          : {}'.format(itemType))
                print('Stackable     : {}'.format(stackable))
                print('Is Broken     : {}'.format(isBroken))
                print('\n[{}{}{}] : Equip'.format(textColor['grn_b'], 'e', textColor[defaultColor]))
                print('[{}{}{}] : Back'.format(textColor['grn_b'], 'b', textColor[defaultColor]))
                



        

        class item:

            def itmDisplay1(targetItem):
                if targetItem == None:
                    display = '---'
                else:
                    name = targetItem['name']
                    tier = itmTierName[targetItem['tier']]
                    colorStart = textColor[itmTierColor[targetItem['tier']]]
                    colorStop = textColor[defaultColor]
                    display = ('{}{}{} ({}{}{})').format(colorStart, name, colorStop, colorStart, tier, colorStop)
                    # display = ('{}{}{}').format(colorStart, name, colorStop)
                return display


            def itmDisplayShort(targetItem):
                if targetItem == None:
                    display = '---'
                else:
                    name = targetItem['name']
                    colorStart = textColor[itmTierColor[targetItem['tier']]]
                    colorStop = textColor[defaultColor]
                    display = ('{}{}{}').format(colorStart, name, colorStop)
                    # display = ('{}{}{}').format(colorStart, name, colorStop)
                return display
        
        class spell:

            def spllDisplay1(targetspell):
                name = targetspell['name']
                tier = itmTierName[targetspell['tier']]
                colorStart = textColor[itmTierColor[targetspell['tier']]]
                colorStop = textColor[defaultColor]
                # display = ('{}{}{} ({}{}{})').format(colorStart, name, colorStop, colorStart, tier, colorStop)
                display = ('{}{}{}').format(colorStart, name, colorStop)
                return display

        
        class enm: 

            def enemyHpBar(enemy):
                hp = enemy['stats']['hp']
                hpMax = enemy['stats']['hpMax']
                fullBar = 30 # length healthbar chars
                text = 'HEALTH '
                char = '■'
                if hp < 0.20 * hpMax:
                    colorStart = textColor['red_b']
                    colorStop = textColor[defaultColor]
                elif hp < 0.40 * hpMax:
                    colorStart = textColor['org_b']
                    colorStop = textColor[defaultColor]
                else:
                    colorStart = textColor['grn_b']
                    colorStop = textColor[defaultColor]

                disp1 = (str(text) + ": (" + colorStart + str(hp) + colorStop + "/" + colorStart + str(hpMax) + colorStop + ")" + colorStop)
                percentageBar = round((hp / hpMax) * 100)
                barNum = round(fullBar*(percentageBar/100))
                disp2 = ("[" + (str(colorStart + (char) + colorStop) * barNum + ("." * round(fullBar-barNum)) + "]"))
                display = (disp1 + " " + disp2)
                return display

            def enemyStats(enemy):
                graphics.line()
                print('ENEMY STATS')
                print('\nName      : {}'.format(enemy['general']['name']))
                print('Level     : {}'.format(enemy['stats']['level']))
                weapon = graphics.ui.item.itmDisplay1(enemy['loadout']['weapon']) 
                armor = graphics.ui.item.itmDisplay1(enemy['loadout']['armor']) 
                shield = graphics.ui.item.itmDisplay1(enemy['loadout']['shield']) 
                print('Creature  : {}'.format(enemy['general']['creature']))
                print('\n{}\n'.format(enemy['general']['description']))
                print(graphics.ui.enm.enemyHpBar(enemy))
                print('\nLoadout:')
                print('- Weapon : {}'.format(weapon))
                print('- Armor  : {}'.format(armor))
                print('- Shield : {}'.format(shield))
                print('\nStrength : {}'.format(enemy['stats']['str']))
                print('Speed    : {}'.format(enemy['stats']['spd']))
                graphics.line()
        

        class combat:

            def combatMessage1(enemy):
                clr = textColor['red_b']
                stop = textColor[defaultColor]
                graphics.clear()
                graphics.line()
                messageList1 = ['{}{}{} has approached your location!', '{}{}{} has blocked your path!', 'You have angered {}{}{}!']
                messageList2 = ['You are now batteling!', 'You will fight it!', 'The battle begins!', 'Hold your ground!', 'Crush them!']
                print(str(messageList1[random.randint(0, 2)].format(clr, enemy['general']['name'], stop)))
                graphics.click()
                print('You have entered combat with {}{}{}'.format(clr, enemy['general']['name'], stop))
                graphics.click()
                print(str(messageList2[random.randint(0, 4)]))
                graphics.click()
            

            def combatMenuTop(player, enemy):
                graphics.clear()
                graphics.line()
                clr1 = textColor['red_b']
                clr2 = textColor['grn_b']
                stop = textColor[defaultColor]
                enmName = enemy['general']['name']
                print('{}{}{}'.format(clr1, enmName, stop))
                print('\nLEVEL  : {}\n'.format(player['stats']['level']))
                print(graphics.ui.enm.enemyHpBar(enemy))
                print(graphics.ui.playerUI.playerArBar(enemy))
                print(graphics.ui.playerUI.playerShBar(enemy))
                print('')
                graphics.line()
                plrName = player['general']['name']
                print('{}{}{}'.format(clr2, plrName, stop))
                print('\nLEVEL  : {}\n'.format(player['stats']['level']))
                print(graphics.ui.playerUI.playerHealthbar(player))
                print(graphics.ui.playerUI.playerArBar(player))
                print(graphics.ui.playerUI.playerShBar(player))
                print('')
                print(graphics.ui.playerUI.playerEpbar(player))
                print(graphics.ui.playerUI.playerMpbar(player))
                print(graphics.ui.playerUI.playerXpbar(player))
                print('')
                graphics.line()
            

            def combatMenu(player, enemy):
                # graphics.clear()
                graphics.ui.combat.combatMenuTop(player, enemy)
                playerInv = player['inventory']
                playerStats = player['stats']
                playerLoadout = player['loadout']
                clr1 = textColor['grn_b']
                clr2 = textColor['ylw_b']
                stop = textColor[defaultColor]
                stats = player['stats']

                print('BATTLE MENU\n')
                print('[{}1{}] : Use {} (EP: -{}{}{})'.format(clr1, stop, graphics.ui.item.itmDisplayShort(playerLoadout['weapon']), clr2, playerLoadout['weapon']['epCost'], stop))
                print('[{}2{}] : Use Spells'.format(clr1, stop))
                print('[{}3{}] : Manage Loadout'.format(clr1, stop))
                print('[{}4{}] : Inventory\n'.format(clr1, stop))
            


