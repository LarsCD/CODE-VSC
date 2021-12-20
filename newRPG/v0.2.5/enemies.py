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
            'weapon': itemDataList['weapons'][9],
            'armor': None,
            'shield': None,
        }, 

        'loot': [
            # [spawnChance, item]
            [0.80, itemDataList['potions'][4]],
            [1.00, itemDataList['weapons'][7]],
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
            'weapon': itemDataList['weapons'][5],
            'armor': itemDataList['armor'][4],
            'shield': itemDataList['shields'][0],
        }, 

        'loot': [
            # [spawnChance, item]
            [0.80, itemDataList['potions'][0]],
            [0.35, itemDataList['weapons'][5]],
        ],
    },

    {
        
    },
]

