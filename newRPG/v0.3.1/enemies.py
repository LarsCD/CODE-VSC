# enemies

from items import *

enemyDataList = [

    {
        'id': 0,

        'general': {
            'name': 'Egg',
            'creature': 'Egg',
            'type': 'bossEnemy',
            'description': 'Egg..?',
        },

        'stats': {
            'level': 1,
            'lvlRange': 40,
            'hp': 50,
            'hpMax': 50,
            'baseHp': 50,
            'str': 5,
            'spd': 5,
            'healFactor': 0.20,
        },

        'loadout': {
            'weapon': ['weapon', 5],
            'armor': ['armor', 0],
            'shield': ['shield', 0],
        }, 

        'lootTable': [
            # [spawnChance, item]
            [0.80, ['potion', 0]],
            [0.35, ['weapon', 5]],
        ],
    },

    {
        'id': 1,

        'general': {
            'name': 'Small Ork',
            'creature': 'Ork',
            'type': 'basicEnemy',
            'description': '\"Small Orks are the smallest of all Orks, or something.\nThey\'re not that smart and are fairly weak.\"',
        },

        'stats': {
            'level': 1,
            'lvlRange': 10,
            'hp': 50,
            'hpMax': 50,
            'baseHp': 50,
            'str': 4,
            'spd': 3,
            'healFactor': 0.30,
        },

        'loadout': {
            'weapon': ['weapon', 5],
            'armor': ['armor', 0],
            'shield': ['shield', 0],
        }, 

        'lootTable': [
            # [spawnChance, item]
            [0.80, ['potion', 0]],
            [0.35, ['weapon', 5]],
        ],
    },

    {
        
    },
]

