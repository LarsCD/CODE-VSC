
import pickle
import sys

from debug import *
from rpgMain import thisDir, system


class saveReader:


    def readSaveFile(saveNr):
        # try:
        debug.log('s', '____________________________________')
        debug.log('s', 'saveReader_readSaveFile start\n')
        loadedData = saveReader.loadData(saveNr)
        saveReader.printSaveData(loadedData)
        print('\n' * 5)
        # except Exception as e:
        debug.log('e', 'readSaveFile')

    def readSaveFileSimple(saveNr):
        debug.log('s', '____________________________________')
        debug.log('s', 'saveReader_readSaveFile start\n')
        loadedData = saveReader.loadData(saveNr)
        print(loadedData)
        print('\n' * 5)




    def printSaveData(loadedData):

        def printSettings(settings_data):
            print()
            debug.log('s', 'SETTINGS:___________________________\n')
            for dataItem in settings_data:
                strSpace = 21 - len(dataItem)
                debug.log('s', '{}{} : {}'.format(dataItem, (' ' * strSpace), settings_data[dataItem]))


        def printOptions(options_data):
            print('\n')
            debug.log('s', 'OPTIONS:___________________________\n')
            for cat in options_data:
                debug.log('s', '{}_OPTIONS:'.format(cat.upper()))
                for dataItem in options_data[cat]:
                    strSpace = 21 - len(dataItem)
                    debug.log('s', '{}{} : {}'.format(dataItem, (' ' * strSpace), options_data[cat][dataItem]))


        def printPlayer(player_data):
            print('\n')
            debug.log('s', 'PLAYER_DATA:___________________________')
            for cat in player_data:
                print()
                debug.log('s', '{}:'.format(cat.upper()))
                if cat == 'general' or cat == 'stats' or cat == 'data':
                    for dataItem in player_data[cat]:
                        strSpace = 21 - len(dataItem)
                        debug.log('s', '{}{} : {}'.format(dataItem, (' ' * strSpace), player_data[cat][dataItem]))
                elif cat == 'inventory':
                    for dataItem in player_data[cat]:
                        strSpace = 21 - len(dataItem)
                        debug.log('s', '{}{} : _category'.format(dataItem, (' ' * strSpace)))
                elif cat == 'loadout':
                    if dataItem == None:
                        dataItem = {'None': 'None'}
                        strSpace = 21 - len(dataItem)
                        debug.log('s','{}{} : _{}'.format(dataItem, (' ' * strSpace), player_data[cat][dataItem]['name']))
                    else:
                        for dataItem in player_data[cat]:
                            if dataItem == None:
                                dataItem = {'None': 'None'}
                                strSpace = 21 - len(dataItem)
                                debug.log('s', '{}{} : _{}'.format(dataItem, (' ' * strSpace),player_data[cat][dataItem]['name']))
                            else:
                                strSpace = 21 - len(dataItem)
                                debug.log('s', '{}{} : _{}'.format(dataItem, (' ' * strSpace), player_data[cat][dataItem]['name']))


        settings = loadedData['settings']
        options = loadedData['options']
        playerData = loadedData['playerData']

        printSettings(settings)
        printOptions(options)
        printPlayer(playerData)




    def loadData(saveNr):
        # COPY OF MAIN FUNC FILE
        def loadDataPrint(loadedData):
            loadDataSize = sys.getsizeof(loadedData)
            debug.log('s', 'save nr.      : {}'.format(saveNr))
            debug.log('s', 'loadData size : {}b\n'.format(loadDataSize))

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
            system.initSystemData(systemData)
            debug.log('s', ('{} successfully loaded').format(targetSave))
            loadDataPrint(loadedData)

        return loadedData