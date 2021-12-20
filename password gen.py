import time, datetime



alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 
						'g', 'h', 'i', 'j', 'k', 'l', 
						'm', 'n', 'o', 'p', 'q', 'r', 
						's', 't', 'u', 'v', 'w', 'x', 
						'y', 'z']


def genPassList4():
    password = ''
    crackPass = '0920'
    list = []
    log = []
    i = 0
    t1 = time.time()
    print('> [generating password...]')
    for n0 in range(36):
        char0 = alphabet[n0]
        i += 1
        for n1 in range(36):
            char1 = alphabet[n1]
            i += 1
            for n2 in range(36):
                char2 = alphabet[n2]
                i += 1
                for n3 in range(36):
                    char3 = alphabet[n3]
                    i += 1
                    for n4 in range(36):
                        char4 = alphabet[n4]
                        i += 1
                        for n5 in range(36):
                            char5 = alphabet[n5]
                            i += 1
                            password = str(f'{char0}{char1}{char2}{char3}{char4}{char5}')
                            # list.append(password)
                    
            progress = round((((i + 1) / (36*36*36*36*36*36)) * 100), 1)
            i_mil = round((i / 1000000), 2)
            logStr = (f'generated: {i_mil} million passwords  -  progress: {progress}%')
            log.append(logStr)
            # console.clear()
            # print('> [generating password...]')
            print(logStr)
                        
    t2 = time.time()
    dt = round((t2 - t1), 2) 
    print(f'> [generated] - time: {dt}s')
    return list, log
        
        




def additionTest():
    stepSize = 100000000
    i = 0
    x = 0
    t1 = 0
    dt = 0
    while True: 
        i += 1
        if i == (x + stepSize):        
            t2 = time.time()
            dt = round((t2 - t1), 3) 
            t1 = time.time()
            x += stepSize
            dtime = datetime.datetime.now()
            print(f'[{dtime}]: [{(i / 1000000000)}billion] - [dt: {dt}s] - [stepsize: {stepSize}]')
        # print(f'{[i]} - [dt: {dt}s]')
    

passwordList, log = genPassList4()
