
# import colorama
import keyboard
import random
from carDatastruct import *

# colorama.init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


class Car:
    def __init__(self, carData, driverData, tyreData):
        carData['general']['number'] = driverData['number']
        carData['driverData'] = driverData
        carData['tyre'] = tyreData
        carData['current']['mult'] = carData['tyre']['tyreMult']
        carData['current']['speed'] = carData['stats']['baseSpeed'] * carData['current']['mult']
        carData['current']['status'] = 'OK'
        self.carData = carData
    
    
class UpdateCarLap:
    def __init__(self, carData):

        # TYRE
        if carData['tyre']['tyreLife'] <= carData['tyre']['tyreFailurePoint']:
            rand = random.randint(0, 100)
            if rand >= 60:
                carData['tyre']['puncture'] = True
        if carData['tyre']['puncture'] == False:
            carData['tyre']['tyreLapsOld'] += 1
            carData['tyre']['tyreLife'] = round((carData['tyre']['tyreLife'] - carData['tyre']['tyreDrain_p_lap']), 1)
            if carData['tyre']['tyreLife'] <= carData['tyre']['tyreDropoffPoint']:
                carData['tyre']['tyreMult'] = round((carData['tyre']['tyreMult'] - carData['tyre']['tyreDropoff']), 3)
            carData['current']['status'] = 'OK'
        else:
            carData['current']['status'] = 'PUNCTURE!'
            carData['tyre']['tyreMult'] = 0.45


        # POWER
        extraPower = 0.0
        if carData['systems']['ERS']:
            if carData['resources']['ERS'] >= carData['stats']['ERSDrain_p_lap']:
                extraPower += carData['stats']['ERSMult']
                carData['resources']['ERS'] -= carData['stats']['ERSDrain_p_lap']
        elif carData['systems']['ERSCharge']:
            carData['resources']['ERS'] += carData['stats']['ERSCharge_p_lap']
        if carData['systems']['DRS']:
            extraPower += carData['stats']['DRSMult']

        carData['current']['mult'] = round(carData['tyre']['tyreMult'] + extraPower, 3)
        carData['current']['speed'] = round((carData['stats']['baseSpeed'] * (carData['current']['mult'])), 1)


        # FUEL
        carData['resources']['fuel'] = round((carData['resources']['fuel'] - carData['stats']['fuelDrain_p_lap']), 2)

        self.carData = carData




def displayCar(carObject):
    display = f'''
------------------------------------------------
[General]     
Car                  {carObject['general']['name']}   
Driver               {carObject['driverData']['name']}
Initials             {carObject['driverData']['initials']}

[Speed] 
Base speed           {carObject['stats']['baseSpeed']} km/h
Actual speed         {(carObject['current']['speed'])} km/h 
Speed multiplier     {(carObject['current']['mult'])}  

[Tyres]
Tyre type            ({carObject['tyre']['tyre']})
Tyre age             {carObject['tyre']['tyreLapsOld']} laps
Tyre life            {carObject['tyre']['tyreLife']}%
Tyre wear            -{carObject['tyre']['tyreDrain_p_lap']}% p/lap  
Tyre multiplier      {carObject['tyre']['tyreMult']}

[Systems]
ERS                  {carObject['resources']['ERS']} kW
FUEL                 {carObject['resources']['fuel']} liter

STATUS               [{carObject['current']['status']}]
------------------------------------------------
'''
    print(display)

def displayCarCompact(carObject):
    display = f'''
------------------------------------------------    
Car            |     {carObject['general']['name']}   
Driver         |     {carObject['driverData']['name']}
Initials       |     {carObject['driverData']['initials']}
------------------------------------------------
Speed          |     {(carObject['current']['speed'])} km/h   
------------------------------------------------
Tyre type      |     ({carObject['tyre']['tyre']})
Tyre age       |     {carObject['tyre']['tyreLapsOld']} laps
Tyre life      |     {carObject['tyre']['tyreLife']}% 
------------------------------------------------
ERS            |     {carObject['resources']['ERS']} kW
FUEL           |     {carObject['resources']['fuel']} liter
------------------------------------------------
STATUS         |     [{carObject['current']['status']}]
------------------------------------------------
'''
    print(display)


def updateCarObject(oldCarObject):
    newCarObject = UpdateCarLap(oldCarObject)
    return newCarObject


car1 = Car(cars['mercedesCarData'], drivers['driver1_name'], tyres['hard'])

for i in range(0, 40):
    print(f'LAP {i}')
    displayCarCompact(car1.carData)
    updateCarObject(car1.carData)

