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
        'ep': 10,
        'epMax': 10,
        'mp': 10,
        'mpMax': 10,
        'str': 5,
        'spd': 5,
        'int': 5,

        'itemCount': 0,
        'itemsMax': 10,
        'spellCount': 0,
        'spellsMax': 100,
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
        'keyItems': [],
        'spells': [],
    },

    'data': {
        'isInCombat': False,
    },
}
