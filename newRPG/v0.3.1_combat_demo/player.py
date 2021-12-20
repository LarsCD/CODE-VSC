# player

playerData = {
    'general': {
        'name': '#playerName',
        'character': '#character', # knight, mage, ect...
    },

    'stats': {
        'level': 1,
        'hp': 100,
        'hpMax': 100,
        'xp': 0,
        'xpMax': 50,
        'ep': 99999,
        'epMax': 99999,
        'mp': 99999,
        'mpMax': 99999,
        'str': 5,
        'spd': 5,
        'int': 5,
    },

    'loadout': {
        'weapon': None,
        'armor': None,
        'shield': None,
    },

    'inventory': {
        'gold': 0,
        'potions': [],
        'weapons': [],
        'armor': [],
        'shields': [],
        'spells': [],
        'keyItems': [],
    },

    'data': {
        'locationID': None,
        'objectiveMessage': 'placeHolder_objective',
    },

    'flags':{
        'isInCombat': False,
    },
}
