# items

itemDataList = {
    'potions': 
    [
        {
            'id': 0,
            'name': 'Normal Potion',
            'type': 'potion',
            'healing': 50,
            'value': 50,
            'stackable': True,
            'tier': 1,  
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 1,
            'name': 'Powerful Potion',
            'type': 'potion',
            'healing': 150,
            'value': 100,
            'stackable': True,
            'tier': 2, 
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 2,
            'name': 'Super Potion',
            'type': 'potion',
            'healing': 350,
            'value': 250,
            'stackable': True,
            'tier': 3, 
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 3,
            'name': 'Hyper Potion',
            'type': 'potion',
            'healing': 550,
            'value': 400,
            'stackable': True,
            'tier': 4, 
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 4,
            'name': 'Max Potion',
            'type': 'potion',
            'healing': 9999,
            'value': 600,
            'stackable': True,
            'tier': 5, 
            'quantity': 0,
            'index': 0,
        }
    ],

    'weapons':[
        {
            'id': 5,
            'name': 'Sword I',
            'type': 'weapon',
            'damage': [10, 24],
            'epCost': 3,
            'critChance': 0.15,
            'value': 200,
            'stackable': False,
            'tier': 1,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 6,
            'name': 'Sword II',
            'type': 'weapon',
            'damage': [25, 34],
            'epCost': 5,
            'critChance': 0.13,
            'value': 450,
            'stackable': False,
            'tier': 2,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 7,
            'name': 'Sword III',
            'type': 'weapon',
            'damage': [35, 44],
            'epCost': 10,
            'critChance': 0.11,
            'value': 650,
            'stackable': False,
            'tier': 3,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 8,
            'name': 'Sword IV',
            'type': 'weapon',
            'damage': [45, 54],
            'epCost': 20,
            'critChance': 0.09,
            'value': 1200,
            'stackable': False,
            'tier': 4,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 9,
            'name': 'Sword V',
            'type': 'weapon',
            'damage': [55, 65],
            'epCost': 40,
            'critChance': 0.07,
            'value': 1700,
            'stackable': False,
            'tier': 5,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 10,
            'name': 'Small Ork Sword',
            'type': 'weapon',
            'damage': [5, 12],
            'epCost': 2,
            'critChance': 0.10,
            'value': 100,
            'stackable': False,
            'tier': 1,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 11,
            'name': 'Medium Ork Sword',
            'type': 'weapon',
            'damage': [12, 25],
            'epCost': 3,
            'critChance': 0.10,
            'value': 100,
            'stackable': False,
            'tier': 2,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 69,
            'name': 'EGG',
            'type': 'weapon',
            'damage': [30, 40],
            'critChance': 0.25,
            'value': 1,
            'stackable': False,
            'tier': 5,
            'quantity': 0, 
            'index': 0,
        },
    ],

    'armor': [
        {
            'id': 12,
            'name': 'Armor I',
            'type': 'armor',
            'hp': 25,
            'hpMax': 25,
            'disperse': 0.50,
            'value': 200,
            'stackable': False,
            'isBroken': False,
            'tier': 1,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 13,
            'name': 'Armor II',
            'type': 'armor',
            'hp': 75,
            'hpMax': 75,
            'disperse': 0.54,
            'value': 400,
            'stackable': False,
            'isBroken': False,
            'tier': 2,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 14,
            'name': 'Armor III',
            'type': 'armor',
            'hp': 150,
            'hpMax': 150,
            'disperse': 0.58,
            'value': 600,
            'stackable': False,
            'isBroken': False,
            'tier': 3,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 15,
            'name': 'Armor IV',
            'type': 'armor',
            'hp': 300,
            'hpMax': 300,
            'disperse': 0.62,
            'value': 800,
            'stackable': False,
            'isBroken': False,
            'tier': 4,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 16,
            'name': 'Armor V',
            'type': 'armor',
            'hp': 600,
            'hpMax': 600,
            'disperse': 0.66,
            'value': 1000,
            'stackable': False,
            'isBroken': False,
            'tier': 5,
            'quantity': 0,
            'index': 0,
        },
    ],

    'shields': [
        {
            'id': 17,
            'name': 'Shield I',
            'type': 'shield',
            'hp': 25,
            'hpMax': 25,
            'disperse': 0.70,
            'value': 100,
            'stackable': False,
            'isBroken': False,
            'tier': 1,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 18,
            'name': 'Shield II',
            'type': 'shield',
            'hp': 50,
            'hpMax': 50,
            'disperse': 0.77,
            'value': 200,
            'stackable': False,
            'isBroken': False,
            'tier': 2,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 19,
            'name': 'Shield III',
            'type': 'shield',
            'hp': 100,
            'hpMax': 100,
            'disperse': 0.84,
            'value': 300,
            'stackable': False,
            'isBroken': False,
            'tier': 3,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 20,
            'name': 'Shield IV',
            'type': 'shield',
            'hp': 150,
            'hpMax': 150,
            'disperse': 0.91,
            'value': 400,
            'stackable': False,
            'isBroken': False,
            'tier': 4,
            'quantity': 0,
            'index': 0,
        },

        {
            'id': 21,
            'name': 'Shield V',
            'type': 'shield',
            'hp': 200,
            'hpMax': 200,
            'disperse': 0.98,
            'value': 500,
            'stackable': False,
            'isBroken': False,
            'tier': 5,
            'quantity': 0,
            'index': 0,
        },
    ],
}
