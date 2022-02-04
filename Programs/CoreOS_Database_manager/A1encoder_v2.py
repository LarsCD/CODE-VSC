# A1encoder 

# functions:
    
# save data to file:    A1encoder.writeToFile(filename, data, key)
# load data from file:  A1encoder.loadFromFile(filename, key)
# encode string:        A1encoder.encode(string, key)
# decode string:        A1encoder.decode(encodedString, key)
# print data:           A1encoder.printData(datadump, filename, key)


import math, time, pickle, os, sys, datetime


currentDir = os.path.dirname(os.path.abspath(__file__))

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

def octal_to_decimal(num):
    decimal_value = 0
    base = 1

    while (num):
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value

def decimal_to_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
    return octal



def encodeProtocalA(string, key):
    t0 = time.time()
    if key < A1encoder.key[0] or key > A1encoder.key[1]:
        print('> [ERROR]: invalid key')
    else:
        # encoding sequence
        stringx = string.encode()
        strByte = int_from_bytes(stringx)
        # type(strByte)
        octKey = decimal_to_octal(key)
        octStrByte = decimal_to_octal(strByte)
        # strByte2 = octal_to_decimal(octStrByte)
        encodedStr = octStrByte + octKey
        # print(f'> [{A1encoder.name}]: strByte: {strByte} / octStrByte: {octStrByte} / octKey: {octKey} / encodedStr: {encodedStr}')

        t1 = time.time()
        dt = round(((t1 - t0)*1000), 2) 
        return encodedStr



def decodeProtocalA(encodedStr, key):
    t2 = time.time()
    encodedInt = int(encodedStr)
    if int(key) < A1encoder.key[0] or int(key) > A1encoder.key[1]:
        print('> [ERROR]: invalid key')
    else:
        try:
            decKey = decimal_to_octal(key)
            decodedInt = octal_to_decimal(encodedInt - decKey)

            if decodedInt != round(decodedInt):
                return '�'
            else: 
                # decodedInt = round(c1 / 4)
                strAsByte = int_to_bytes(decodedInt)
                decodedStr = strAsByte.decode()
                t3 = time.time()
                dt = round(((t3 - t2)*1000), 2)
                return decodedStr
        except UnicodeDecodeError:
            # print('> [ERROR]: improper decoding 1')
            return '▒'



class A1encoder:

    name = 'A1_ENCODER'
    model = 'CoreOS:A1encoder series'
    key = (0, 1000)
    protocal = 'CoreOS:PROT:A'
    product = 'CoreOS:A1encoder'
 
       
    def __init__(self):
        print(f'> [{self.name}]: STATUS: ACTIVE\n')
        

    def encode(string, key):
        print(f'> [{A1encoder.name}]: encoding data...')
        t0 = time.time()
        encodedStringList = []
        for char in string:
            encodedInt = encodeProtocalA(char, key)
            encodedStringList.append(str(encodedInt))
        t1 = time.time()
        dt = round(((t1 - t0)), 3)
        print(f'> [{A1encoder.name}]: data encoded - time: {dt}s')
        return encodedStringList
    
    
    def decode(encodedString, key):
        print(f'> [{A1encoder.name}]: decoding data...')
        t0 = time.time()
        decodedStringList = []
        for int in encodedString:
            decodedInt = decodeProtocalA(int, key)
            decodedStringList.append(str(decodedInt))
        decodedMessage = ''.join(decodedStringList)
        # print(decodedMessage)
        t1 = time.time()
        dt = round(((t1 - t0)), 3)
        print(f'> [{A1encoder.name}]: data decoded - time: {dt}s')
        return decodedStringList  


    def writeToFile(filename, data, key):
        t0 = time.time()
        print(f'\n> [{A1encoder.name}]: [!!] writeToFile \'{filename}\'...')
        data = str(data)
        encodedData = A1encoder.encode(data, key)
        outfile = open(os.path.join(currentDir, filename), 'wb')
        print(f'> [{A1encoder.name}]: writing data to file: \'{filename}\'...')
        pickle.dump(encodedData, outfile) # 16/12/2022: not working?
        outfile.close()  
        t1 = time.time()
        dt = round(((t1 - t0)), 3)
        print(f'> [{A1encoder.name}]: data succesfully writen - time: {dt}s\n')
        return encodedData
    
    
    def loadFromFile(filename, key):
        t0 = time.time()
        # infile = open(filename, 'rb')
        # outfile = open(filename,'wb')
        print(f'\n> [{A1encoder.name}]: [!!] loadFromFile \'{filename}\'...')
        print(f'> [{A1encoder.name}]: loading data to file: \'{filename}\'...')       
        infile = open(os.path.join(currentDir, filename),'rb')
        encodedData = ''
        try: 
            encodedData = pickle.load(infile)
        except EOFError: 
            t1 = time.time()
            dt = round(((t1 - t0)), 3)
            print(f'\n> [ERROR]: file \'{filename}\' contains no data')
            print(f'> [{A1encoder.name}]: error in loading data - time: {dt}s\n')          
        else: 
            decodedData = A1encoder.decode(encodedData, key)  
            t1 = time.time()
            dt = round(((t1 - t0)), 3)
            print(f'> [{A1encoder.name}]: data succesfully loaded - time: {dt}s\n')           
            return decodedData
    
    
    def printData(datadump, filename, key): 
        size = sys.getsizeof(datadump)
        suffix = 'b'
        if size > 1100:
            size = round((sys.getsizeof(datadump) / 1000), 2)
            suffix = 'kb'
        path = os.path.join(currentDir, filename)
        print(f'''------------------------------------------------------------
File: {filename}
Size: {size}{suffix}
Key: {key}''')
        print('------------------------------------------------------------')
        decodedMessage = ''.join(datadump)
        print(decodedMessage)
        print('------------------------------------------------------------')


    def processDataString(datadump):
        data = ''.join(datadump)
        return data

A1encoder()
