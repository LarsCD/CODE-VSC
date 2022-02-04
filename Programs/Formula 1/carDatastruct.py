
cars = {
    'mercedesCarData': {
        'general': {
            'name': 'Mercedes F1 car',
            'color': 'CYAN',
            'number': 0,
        },
        'driverData': {},
        
        'resources': {
            'ERS': 120,  # kW
            'fuel': 145, # l
        },
        'systems': {
            'ERS': True, # enabled
            'DRS': False, # enabled
            'ERSCharge': False, # enabled
        },
        'current': {
            'speed': 0,
            'mult': 0,
            'status': 'STATUS',
        },
        'tyre': {},

        'stats': {
            'baseSpeed': 320, # km/h
            'ERSMult': 0.12, # +%
            'DRSMult': 0.09, # +%
            
            'ERSCharge_p_lap': 75, # kW
            'ERSDrain_p_lap': 100, # kW
            'fuelDrain_p_lap': 2.6, # l                     
        }
    },
}


tyres = {
    'soft': {
        'tyre': 'S',
        'tyreLife': 100, # %
        'tyreMult': 1.04, # *%
        'tyreLapsOld': 0, # laps
        'puncture': False,
        
        'tyreDrain_p_lap': 3.75, # % p/lap
        'tyreFailurePoint': 43.75, # % wear / 15 laps (S)
        'tyreDropoffPoint': 62.5,  # % wear / 10 laps (S) 66.6% of failure
        'tyreDropoff': 0.01, # -mult p/lap / tyre mult 0.89 at failure
    },
    
    'medium': {
        'tyre': 'M',
        'tyreLife': 100, # %
        'tyreMult': 1.01, # *%
        'tyreLapsOld': 0, # laps
        'puncture': False,
        
        'tyreDrain_p_lap': 2.25, # % p/lap
        'tyreFailurePoint': 32.5,  # % wear / 30 laps (M)
        'tyreDropoffPoint': 59.5,  # % wear / 18 laps (M) 60.0% of failure
        'tyreDropoff': 0.006, # -mult p/lap / tyre mult 0.83 at failure
    },
    
    'hard': {
        'tyre': 'H',
        'tyreLife': 100, # %
        'tyreMult': 0.99, # *%
        'tyreLapsOld': 0, # laps
        'puncture': False,

        'tyreDrain_p_lap': 1.55, # % p/lap
        'tyreFailurePoint': 45.75, # % wear / 40 laps (H)       
        'tyreDropoffPoint': 56.6,  # % wear / 28 laps (H) 70.0% of failure             
        'tyreDropoff': 0.003, # -mult p/lap / tyre mult 0.87 at failure
    },
}


drivers = {
    'driver1_name': {
        'name': 'Max Verstappen',
        'initials': 'VER',
        'number': '33',
        'stats': {
            'exp': 66,
            'rc': 94,
            'awar': 85,
            'pace': 98,
        }        
    },
}
