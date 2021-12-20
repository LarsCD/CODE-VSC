import base64
import pickle
import os
from os import listdir
from os.path import isfile, join
import sys
import datetime
import time
import glob
from pathlib import Path
import traceback


# //// GLOBAL DATA ////
thisDir = os.getcwd()
thisFileName = str(os.path.basename(__file__)).replace('.py', '')


systemData = {
	'debugMode': True,
	'firstTimeOpen': True,
	'initialLoad': False,
	'defaultKey':  0,
	'passCode': 0,
	'runOnPC': True,
	'resCols': 120,
	'resLines': 45,
	'dirs': [],
	'entries': {},
}


if systemData['runOnPC'] == False:
	import console


class debug():
	def printLine():
		if systemData['runOnPC'] == True:
			print('- ' * round(systemData['resCols'] / 2))
		else: 
			print('- ' * 39)
	
	def clear():
		if systemData['runOnPC'] == True:
			os.system('clear')
		else:
			console.clear()
	
	def setResolution():
		if systemData['runOnPC'] == True:
			os.system('mode con cols=' + str(systemData['resCols']) + 'lines=' + str(systemData['resLines']))
		else:
			pass


class b64Code:
	
	def encode64(text):			
		message = str(text)
		message_bytes = message.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')		
		return base64_message
			
			
	def decode64(b64Text):		
		base64_message = str(b64Text)
		base64_bytes = base64_message.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		message = message_bytes.decode('ascii')				
		return message

		
	def hardEncode(text, key):
		t = datetime.datetime.now()
		try:
			print('\n> Hard encoding message... (key = ' + str(round(key)) + ')')	
			if key > 50:
				print('> ERROR: Invalid Key')	
			else: 
				i = 0
				b64Text = b64Code.encode64(text)
				while i < key:
					b64Text = b64Code.encode64(b64Text)
					i += 1
				t2 = datetime.datetime.now()
				dTime = t2 - t
				ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
				if ms > 999: 
					s = ms / 1000
					print('> Message successfully encoded (' + str(round(s, 1)) + 's)')
				else: 
					print('> Message successfully encoded (' + str(ms) + 'ms)')
				return b64Text
		except UnicodeDecodeError: 
			print('\n> ERROR: encode error')

		
	def hardDecode(b64Text, key):
		t = datetime.datetime.now()
		try:
			print('\n> Hard decoding message... (key = ' + str(round(key)) + ')')	
			if key > 50:
				print('> ERROR: Invalid Key')	
			else: 
				i = 0
				text = b64Code.decode64(b64Text)
				while i < key:
					text = b64Code.decode64(text)
					i += 1
				t2 = datetime.datetime.now()
				dTime = t2 - t
				ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
				if ms > 999: 
					s = ms / 1000
					print('> Message successfully decoded (' + str(round(s, 0)) + 's)')
				else: 
					print('> Message successfully decoded (' + str(ms) + 'ms)')
				return text
		except UnicodeDecodeError: 
			print('\n> ERROR: decode error')
	
	def isBase64(message):
		try:
			return base64.b64encode(base64.b64decode(message)) == message
		except Exception:
			return False



class pathData:
	
	def createPath(dir, fileName):
		fileRelativePath = os.path.join(dir, fileName)
		filePath = os.path.join(thisDir, fileRelativePath)
		entryData.addEntry(dir, filePath)
		# print('\n> Path created: ' + str(filePath))
		print('\n> Path created: ' + fileRelativePath)
		# print('> Saved entry: entries > ' + dir)
		return filePath
		
		
	def returnPath(dir, fileName):	
		fileRelativePath = os.path.join(dir, fileName)
		filePath = os.path.join(thisDir, fileRelativePath)
		return filePath
	
	
	def getFilePaths(dir):
		# gets all file names from dir
		# allFiles = [file for file in listdir(str(dir)) if isfile(join(dir, file))]
		allFiles = []
		for file in listdir(str(dir)):
			if isfile(os.path.join(dir, file)): 
				if 'systemData' in file:  # maybe put saveData in here but honestly I dont wanna find out what happens then...
					pass
					# dont put systemData in entries
				else: 
					allFiles.append(file)
		allEntries = []
		# puts all entries in 'allEntries'
		for file in allFiles:
			entry = pathData.returnPath(dir, file)			
			allEntries.append(entry)	
		return allEntries
	
	
	def getDirPath(): 
		# gets all dirs names from current directory
		rawAllDirs = os.listdir(thisDir)
		try:
			targetFile = thisFileName + '.py'
			rawAllDirs.remove(targetFile)
			rawAllDirs.remove('.DS_Store')
		except:
			pass
		allDirs = rawAllDirs
		return allDirs
			
		
	
	def fileSelector():
		print('\n> Select entry:')		
		# checks if file exists in entries
		i = 1
		for entryDir in systemData['entries']:

			allFiles = []
			for file in listdir(os.path.join(thisDir, entryDir)):
				if isfile(os.path.join(os.path.join(thisDir, entryDir), file)):
					if entryData.checkEntry(entryDir, pathData.returnPath(entryDir, file)) == False:
						# is not in entries
						pass
					else: 
						# is in entries 
						allFiles.append(file)			
			# prints entry list for selection
			fileCount = len(systemData['entries'][entryDir])
			lenDir = len(entryDir)
			stringSpaces = 20 - lenDir
			print('\nAll files in \'' + entryDir + '\':' + (' ' * stringSpaces) + '(file count: ' + str(fileCount) + ')')
			for file in allFiles:
				print(' [' + str(i) + '] ' + file)
				i += 1
		# gathers all entries for selection 
		allEntries = []
		for entryDir1 in systemData['entries'].values():
			for entry in entryDir1:
				allEntries.append(entry)
		while True: 
			try:
				inputEntry = int(input('\n> Select file: '))
			except: 
				print('> Invalid input')
			else: 
				break
		try:
			filePath = allEntries[inputEntry - 1]
		except: 
			return None 
		else:
			return filePath

		
	def createFileSelector():
		print('Dirs:')
		i = 1
		dir = ''
		# loop for dir input
		while True:
			for dir1 in systemData['dirs']:
				print(' [' + str(i) + ']: ' + dir1)
				i += 1
			try: 
				dirInt = int(input('\n> Input file dir number: '))
			except: 
				print('> Invalid input\n')
				time.sleep(1.5)
			else: 				
				if dirInt > len(systemData['dirs']) and dirInt != 0:
					print('> Invalid input\n')
					i = 1
					time.sleep(1.5)
					print('')
				else: 
					dir = systemData['dirs'][dirInt - 1]
					break
		# loop for name input	
		while True:
			fileName = input('> Input file name: ')
			print('> Confirm \'' + str(fileName) + '\'?   (y/n)')
			y_n = input('> Input: ')
			if y_n == 'y':
				break
		return dir, fileName
	
	
	def createDir(dirName): 
		print('\n> [!!] Adding subdir \'' + dirName + '\' to current dir')
		path = os.path.join(thisDir, dirName)
		try:  
			os.mkdir(path)
		except IsADirectoryError: 
			print('\n> Could not create dir \'' + dirName + '\', dir already exists')
		except Exception as e: 
			print('\n> Could not create dir \'' + dirName + '\'')
			print('> Error message:' + str(e))
		if path not in systemData['entries']:
			pathData.addDirToEntry(dirName)
			print('\n> Dir \'' + dirName + '\' created')
		
	
	def removeDir(dirName):
		print('\n> Removing dir \'' + dirName + '\' from current dir')
		path = os.path.join(thisDir, dirName)
		try:  
			os.rmdir(path)
		except OSError as e:
			if e.errno == 66:
				print('\n> Could not remove dir \'' + dirName + '\', dir is not empty')
			else:
				print('\n> Could not remove dir \'' + dirName + '\', dir does not exist')
				
		else: 
			pathData.removeDirEntry(dirName)
			pathData.initDirs()
			# entryData.initEntries()
			print('\n> Dir \'' + dirName + '\' removed')

		
	def addDirToEntry(dirName):
		global systemData
		systemData['entries'].update({dirName: []})
		pathData.initDirs()
		print('\n> Added dir \'' + dirName + '\' to dir list')

		
	def removeDirEntry(dirName):
		global systemData
		systemData['dirs'].remove(str(dirName))
		pathData.initDirs()
		print('\n> Removed dir: \'' + str(dirName) + '\' from dir list')	
		
	
	def initDirs(): 
		# print('\n> initDirs')
		global systemData
		systemData['dirs'] = pathData.getDirPath()
		for dir in systemData['dirs']:
			if dir not in systemData['entries']:
				pathData.addDirToEntry(dir)



class fileData:
		
	def writeFile(path, text):
		t = datetime.datetime.now()
		print('\n\n> [!!] Writing to file...')
		file = open(path, 'a')		
		file.write(str(text + '\n'))
		file.close()
		print('> Wrote // DATA // to ' + path)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		if ms > 999: 
			s = ms / 1000
			print('\n> Write successful (' + str(round(s, 1)) + 's)')
		else: 
			print('\n> Write successful (' + str(round(ms, 1)) + 'ms)')

		
	def writeEncryptedFile(path, text, key):
		t = datetime.datetime.now()
		print('\n\n> [!!] Preparing write to encrypted file...')
		encryptedData = b64Code.hardEncode(str(text), key)
		print('\n> Writing to encrypted file...')
		file = open(path, 'wb')
		pickle.dump(encryptedData, file)
		file.close()
		print('> Wrote // ENCRYPTED DATA // to ' + path)
		t2 = datetime.datetime.now()
		dTime = t2 - t
		ms = round(float((dTime.total_seconds() * 10000) / 10), 1)
		if ms > 999: 
			s = ms / 1000
			print('\n> Write successful (' + str(round(s, 1)) + 's)')
		else: 
			print('\n> Write successful (' + str(round(ms, 1)) + 'ms)')

		
	def returnFileContent(path):
		print('\n\n> [!!] Preparing to read file...')
		# reads file data 
		file = open(path, 'r')	
		try:
			data = file.read()
		except UnicodeDecodeError:
			print('\n> ERROR: cannot read file, file is encrypted')
			print('\n> Read file unsuccessful')
		except Exception as e:
			print('\n> ERROR: cannot read file: ')
			print(str(e))
			print('\n> Read file unsuccessful')
			file.close()
			return None
		else: 
			file.close()
			return data
	
	
	def returnEncryptedContent(path, key):
		print('\n\n> [!!] Preparing to read encrypted file...')
		# reads pickle data and decodes bytes
		file = open(path, 'rb')
		try: 
			unDecryptedData = pickle.load(file)
		except Exception as e: 
			print('\n> File could not be read')
			print('\n> ERROR: ' + str(e))
			
		else: 
			file.close()
			# decrypts decoded pickle data from b64 to text
			try: 
				decryptedData = b64Code.hardDecode(unDecryptedData, key)
			except: 
				print('\n> ERROR: file could not be read because key is invalid')
			else: 
				if decryptedData == None:
					print('\n> ERROR: file could not be read because key is invalid')
					return None
				else: 
					data = decryptedData.strip()
					return data
	
	
	def readFile(path):
		print('\n\n> [!!] Preparing to read file...')
		# reads file data 
		file = open(path, 'r')	
		try:
			data = file.read()
		except UnicodeDecodeError:
			print('\n> ERROR: cannot read, file is encrypted')
			print('\n> Read file unsuccessful')
			file.close()
		else: 
			file.close()
			# displays text
			print('\n> Reading file...\n')
			debug.printLine()
			print('> Contents:     (normal file)\n')
			print(data)
			# for line in lines:
			# 	print(line)
			debug.printLine()
			print('\n')
		
	
	def readEncryptedFile(entryPath, key):
		print('\n\n> [!!] Preparing to read encrypted file...')
		# reads pickle data and decodes bytes
		file = open(entryPath, 'rb')
		try: 
			unDecryptedData = pickle.load(file)
		except: 
			print('> ERROR: trying to decrypt undecryptable file')
			print('\n> File could not be read because file is not encrypted')
		else: 
			file.close()
			# decrypts decoded pickle data from b64 to text
			try: 
				decryptedData = b64Code.hardDecode(unDecryptedData, key)
			except: 
				print('\n> ERROR: file could not be read because key is invalid')
			else: 
				if decryptedData == None:
					print('\n> ERROR: file could not be read because key is invalid')
				else: 
					lines = decryptedData.strip()
					# strips newline character and displays text
					print('\n> Reading encrypted file...\n')
					debug.printLine()
					print('> Contents:     (b64 decoded, key = ' + str(key) + ')\n')
					print(lines)
					debug.printLine()
					print('\n')
			
		
	def createFile(dir, fileName):
		if entryData.checkEntry(dir, fileName) == True: 
			print('> Entry already exists (entry' + dir + '/' + entry + ')')
		else: 
			path = pathData.createPath(dir, fileName)
			file = open(path, 'w').close()
			print('\n> [!!] File created')
			print('\n> File path: ' + path)
			entryData.initEntries()
	
	
	def clearFile(entryPath):
		print('\n> [!!] Clearing file...')
		file = open(entryPath, 'w').close()
		print('> Cleared file \'' + entryPath + '\'')
	
	
	def removeFile(filePath):
		print('\n\n> [!!] Removing file...')
		os.remove(filePath)
		entryData.removeEntry(filePath)
		entryData.initEntries()
		print('\n> File successfully removed')

	

class entryData:
	
	def initEntries(): 
		global systemData
		pathData.initDirs()
		# print('\n> initEntries')
		for i in range(0, 25):
			try:
				systemData['entries'][systemData['dirs'][i]] = pathData.getFilePaths(systemData['dirs'][i])
			except: 
				break # this is fine, dont change, it only jumps outof for loop
			
	
	def printEntryList():
		print('\n> All entries:')		
		# checks if file exists in entries
		allFiles = []
		targetDir = None
		for entryDir in systemData['entries']:
			try:
				targetDir = listdir(os.path.join(thisDir, entryDir))
			except:
				pass
			else:
				for file in targetDir:
					if isfile(os.path.join(os.path.join(thisDir, entryDir), file)):
						if entryData.checkEntry(entryDir, pathData.returnPath(entryDir, file)) == False:
							# is not in entries
							print('\n> ERROR: ' + str(os.path.join(entryDir, file)) + ' not in entries')
							pass
						else: 
							# is in entries 
							allFiles.append(file)
					else: 
						print('\n> ERROR: ' + str(os.path.join(entryDir, file)) + ' doenst exsist...')
			# prints full entry list
			fileCount = len(systemData['entries'][entryDir])
			lenDir = len(entryDir)
			stringSpaces = 20 - lenDir
			print('\nAll files in \'' + entryDir + '\':' + (' ' * stringSpaces) + '(file count: ' + str(fileCount) + ')')
			for file in allFiles:
				print('- ' + file)				
		print('\n')
	
	
	def addEntry(dir, entry):
		entryExists = entryData.checkEntry(dir, entry)
		if entryExists == False:
			systemData['entries'][dir].append(entry)
		else:
			print('\n> Entry already exists (entry' + dir + '/' + entry + ')')

		
	def checkEntry(dir, entry): # ERROR WHEN RUNNING ON PC (NOT IN IDE)
		if entry not in systemData['entries'][dir]:
			return False
		else:
			return True
	
	
	def removeEntry(targetEntry):
		global systemData
		# globalEntries = entries
		print('\n> Removing entry...')
		entryFound = False		
		# goes through all entries in entry list and removes target entry
		for dir in systemData['entries']: # goes through dirs (returns string)
			for entry in systemData['entries'][dir]: # goes through entries
				if entry == targetEntry:					
					entryFound = True
					systemData['entries'][dir].remove(entry)
		# end message
		if entryFound == True: 
			print('\n> Entry successfully removed entry \n\'' + entry + '\'')
		else: 
			print('\n> ERROR: entry does not exist and could not be removed \n\'' + entry + '\'')
		return systemData['entries']



class system: 
	
	class data:
		
		def changePass():
			global systemData
			login = False
			print('\n> Command: [Change autharization code]')
			print('> Input //cancel to cancel autharization code change\n')
			while True: 
				try:
					userInput = input('\n> Input current autharization code: ')
					if '//cancel' in userInput: 
						break
					else: 
						userInput = int(userInput)
				except:
					print('\n> Input must be numbers')
					time.sleep(1.5)
				else: 					
					if int(userInput) == systemData['passCode']:
						login = True
						break
					else: 
						print('\n> Wrong authorization code, reseting...')
						time.sleep(1.5)
			if login == True:
				userInput = input('> New authorization code: ')
				systemData['passCode'] = int(userInput)
				print('\n> Code change successful')
			else: 
				print('\n> Code change unsuccessful')
				
			
		def printDate():
			date = datetime.datetime.now()
			print('DATE: ' + date.strftime("%x"))
			
	
	def startUp():
		try:
			if systemData['debugMode'] == False:
				system.loadData()
		except: 
			pass
		if systemData['initialLoad'] == False:
			system.firstStartSetup()
		if systemData['debugMode'] == False:
			system.loadData()
		debug.setResolution()
		system.login()
		debug.clear()
		debug.printLine()
		system.data.printDate()
		print('\n> System startup...')
		if systemData['debugMode'] == False:
			system.loadData()
		pathData.initDirs()
		entryData.initEntries()
		print('\n> System startup complete')
		debug.printLine()
		entryData.printEntryList()
	
	
	def login():
		tries = 3
		login = False
		userInput = ''
		while tries > 0:
			debug.clear()
			debug.printLine()
			if systemData['debugMode'] == True:
				systemStatus = '(Debug mode)'
			else: 
				systemStatus = ''
			print('  --  ' + thisFileName + '  --  CoreOS  --  Property of LCD  --  ' + systemStatus)
			print('\n\n> SYSTEM AUTHORIZATION REQUIRED      (tries: ' + str(tries) + ')')
			try:
				userInput = int(input('> System authorization code: '))
			except:
				print('\n> Input must be numbers')
				time.sleep(2)
			else: 					
				tries -= 1	
				if int(userInput) == systemData['passCode']:
					login = True
					break
				else: 
					if tries > 0:
						print('\n> Wrong authorization code, reseting...')
						time.sleep(2)
					else: 
						break
		if login == True: 
			print('\n> Login successful')
			time.sleep(2)
		else: 
			print('\n> Closing program...')
			time.sleep(2)
			sys.exit()


	def saveData():
		print('\n\n> [!!] Saving system data...')
		packagedData = systemData
		try: 
			saveDataDirPath = os.path.join('saveData', 'systemData')
			saveDataPath = os.path.join(thisDir, saveDataDirPath)
			file = open(saveDataPath, 'wb')
		except FileNotFoundError:
			print('\n> ERROR: no file to save data to')
		else: 
			pickle.dump(packagedData, file)
			file.close()
			print('\n> System data successfully saved')
		
	
	def loadData():
		print('\n\n> [!!] Loading system data...')
		global systemData
		try:
			saveDataDirPath = os.path.join('saveData', 'systemData')
			saveDataPath = os.path.join(thisDir, saveDataDirPath)
			file = open(saveDataPath, 'rb')
		except FileNotFoundError:
			print('\n> ERROR: no file to load data from')
		else: 
			loadedData = pickle.load(file)
			file.close()
			systemData = loadedData
			print('> System data successfully loaded')
	
	
	def firstStartSetup():
		global systemData
		graphics.UI_clear()
		print('\n> Press [enter] to initialize data')
		pressContinue = input('')
		graphics.UI_clear()
		debug.setResolution()
		time.sleep(0.1)
		graphics.UI_clear()
		print('\n> [!!] Initalizing data...\n')
		time.sleep(0.2)
		pathData.createDir('saveData')
		time.sleep(0.2)
		pathData.createDir('files')
		time.sleep(0.2)
		pathData.createDir('encryptedFiles')
		time.sleep(0.05)
		pathData.initDirs()
		time.sleep(0.05)
		entryData.initEntries()
		time.sleep(0.2)
		fileData.createFile('saveData', 'systemData')
		time.sleep(0.05)
		pathData.initDirs()
		time.sleep(0.05)
		entryData.initEntries()
		time.sleep(0.2)
		systemData['firstTimeOpen'] = False
		systemData['initialLoad'] = True
		system.saveData()
		time.sleep(0.2)
		print('\n\n> Initalizing data successful')
		print('> Press [enter] to continue')
		pressContinue = input('')

	

class graphics:
	
	def UI_help():
		graphics.UI_clear()
		debug.printLine()
		print('COMMAND HELP')
		print('Use //#COMMAND# to execute list commands\n')	
		print('\nCommon Commands:  ')	
		print('- help       : show command help')	
		print('- clear      : clear screen')	
		print('- entry      : show full entry list')	
		print('\n- save       : save system data')	
		print('- load       : load system data')	
		print('\n- exit       : save and exit program')	
		print('\nFile Commands: ')	
		print('- cf         : Create file and write')	
		print('- ce         : Create encrypted file and write')	
		print('\n- rf         : Read file  ')	
		print('- re         : Read encrypted file')	
		print('\n- wf         : Write to file')	
		print('- we         : Write to encrypted file')	
		print('\n- clrf       : Clear file')	
		print('- rmvf       : Remove file')	
		print('\nUse code  to execute system commands \n')	
		debug.printLine()
		
	
	def UI_clear():
		debug.clear()
		debug.printLine()
		system.data.printDate()
	
	
	def UI_entryList():
		graphics.UI_clear()
		debug.printLine()
		entryData.printEntryList()
		debug.printLine()
			


class interface: 
	
	def userPrompt():
		userInput = input('\n> ')	
		if '//help' in userInput:
			graphics.UI_help()
		elif '//clear' in userInput:
			graphics.UI_clear()
		elif '//entry' in userInput:
			graphics.UI_entryList()
		elif '//save' in userInput:
			system.saveData()
		elif '//load' in userInput:
			system.loadData()
		elif '//cf' in userInput:
			graphics.UI_clear()
			interface.createFile()
		elif '//ce' in userInput:
			graphics.UI_clear()
			interface.createEncryptedFile()
		elif '//rf' in userInput:
			graphics.UI_clear()
			interface.readFile()
		elif '//re' in userInput:
			graphics.UI_clear()
			interface.readEncryptedFile()
		elif '//wf' in userInput:
			graphics.UI_clear()
			interface.writeToFile()
		elif '//we' in userInput:
			graphics.UI_clear()
			interface.writeToEncryptedFile()
		elif '//clrf' in userInput:
			interface.clearFile()
		elif '//rmvf' in userInput:
			interface.removeFile()
		elif '//exit' in userInput:
			interface.exit()
		elif '//changePass' in userInput:
			system.data.changePass()
		else:
			try: 				
				exec(userInput)
			except Exception as e: 
				print('\n> ERROR: Command does not exist: ')
				print(str(e))
			
			
	def createFile():
		graphics.UI_clear()
		print('\n> Command: [Create file]')
		dir, fileName = pathData.createFileSelector()
		fileData.createFile(dir, fileName)		
		path = pathData.returnPath(dir, fileName)
		data = interface.writeFunc(path, '')
		graphics.UI_clear()
		fileData.writeFile(path, data)
	
				
	def createEncryptedFile():
		graphics.UI_clear()
		print('\n> Command: [Create encrypted file]')
		dir, fileName = pathData.createFileSelector()
		while True:
			key = input('\n> Input key: ')
			print('> Confirm key = ' + str(key) + '?   (y/n)')
			y_n = input('> Input: ')
			if y_n == 'y':
				break
		fileName = (fileName + ' [ENCODED]')
		fileData.createFile(dir, fileName)		
		path = pathData.returnPath(dir, fileName)
		data = interface.writeFunc(path, '')
		graphics.UI_clear()
		fileData.writeEncryptedFile(path, data, int(key))
	
	
	def writeFunc(path, data):
		while True:
			graphics.UI_clear()
			print('\n> Write to file: ')
			print('> Input //complete to complete and write to file\n')
			print(str(data))
			lineInput = input('> ')
			if lineInput == '//complete':
				break
			else: 
				data = data + str(lineInput + '\n')
		return data

		
	def readFile():	
		graphics.UI_clear()
		print('\n> Command: [Read file]')
		while True: 
			filePath = pathData.fileSelector()
			if filePath == None: 
				print('\n> ERROR: selected file does not exsist\n')
			else: 
				break
		graphics.UI_clear()
		print('\n> Accessing file...')
		fileData.readFile(filePath)
	
				
	def readEncryptedFile():
		graphics.UI_clear()
		print('\n> Command: [Read encrypted file]')		
		while True: 
			filePath = pathData.fileSelector()
			if filePath == None: 
				print('\n> ERROR: selected file does not exsist\n')
			else: 
				break
		while True:
			try: 
				key = int(input('\n> Input key: '))
			except: 
				print('\n> Invalid input, should be numbers only')
			else: 
				print('> Confirm key = ' + str(key) + '?   (y/n)')
				y_n = input('> Input: ')
				if y_n == 'y':
					break
		graphics.UI_clear()
		print('\n> Accessing file...')
		fileData.readEncryptedFile(filePath, key)
	
	
	def writeToFile():
		graphics.UI_clear()
		print('\n> Command: [Write file]')
		while True: 
			filePath = pathData.fileSelector()
			if filePath == None: 
				print('\n> ERROR: selected file does not exsist\n')
			else: 
				break
		graphics.UI_clear()
		print('\n> Accessing file...')
		data = fileData.returnFileContent(filePath)
		if data == None:
			print('\n> ERROR: cannot read file, file is encrypted format')
			print('\n> Read file unsuccessful')
		else: 
			dataNew = interface.writeFunc(filePath, data)
			graphics.UI_clear()
			fileData.clearFile(filePath)
			fileData.writeFile(filePath, dataNew)
	
	
	def writeToEncryptedFile():
		graphics.UI_clear()
		print('\n> Command: [Write encrypted file]')
		while True: 
			filePath = pathData.fileSelector()
			if filePath == None: 
				print('\n> ERROR: selected file does not exsist\n')
			else: 
				break
		while True:
			try: 
				key = int(input('\n> Input key: '))
			except: 
				print('\n> Invalid input, should be numbers only')
			else: 
				print('> Confirm key = ' + str(key) + '?   (y/n)')
				y_n = input('> Input: ')
				if y_n == 'y':
					break
		graphics.UI_clear()
		print('\n> Accessing file...')
		data = fileData.returnEncryptedContent(filePath, key)
		if data == None:
			print('data: None')
			print('\n> Read file unsuccessful')
		else: 
			fileData.readEncryptedFile(filePath, data)
			dataNew = interface.writeFunc(filePath, data)
			graphics.UI_clear()
			fileData.clearFile(filePath)
			fileData.writeEncryptedFile(filePath, dataNew, key)
	
	
	def clearFile():
		graphics.UI_clear()
		print('\n> Command: [Clear file]')
		while True: 
			filePath = pathData.fileSelector()
			if filePath == None: 
				print('\n> ERROR: selected file does not exsist\n')
			else: 
				break
		graphics.UI_clear()
		fileData.clearFile(filePath)
	
	
	def removeFile():
		graphics.UI_clear()
		print('\n> Command: [Remove file]')
		confirm = False
		while True: 
			filePath = pathData.fileSelector()
			if filePath == None: 
				print('\n> ERROR: selected file does not exsist\n')
			else: 
				print('> Confirm remove file?   (y/n)')
				y_n = input('> Input: ')
				if y_n == 'y':
					confirm = True
					break
		if confirm == True:
			graphics.UI_clear()
			fileData.removeFile(filePath)
		else: 
			pass

		
	def exit():
		systemData['firstTimeOpen'] = False
		systemData['initialLoad'] = True
		graphics.UI_clear()
		time.sleep(0.2)
		pathData.initDirs()
		entryData.initEntries()
		time.sleep(0.2)
		system.saveData()
		time.sleep(0.5)
		print('\n> Closing program...')
		time.sleep(1.2)
		sys.exit()		



# //// CODE EXECUTION ////

if systemData['debugMode'] == True:
	# run in debug mode (loads system data from internal systemData)
	system.startUp()
	while True:
		interface.userPrompt()
	
else: 
	# run in normal mode (loads system data from saveData)
	try: 
		# system starup and program loop
		system.startUp()	
		while True:
			interface.userPrompt()	
	except Exception as e:
		debug.printLine()
		# debug.clear()
		traceback.print_exc()
		confirm = False
		while True:
			print('\n> Encountered an error, would you like to re-initialize data (y/n)?')
			y_n = input('> Input: ')
			if y_n == 'y':
				confirm = True
				break
			elif y_n =='n':
				break
		if confirm == True:
			system.firstStartSetup()
			print('\n> System re-initialization successfull, please restart the application...')
			print('> Press [enter] to exit')
			pressContinue = input('')
