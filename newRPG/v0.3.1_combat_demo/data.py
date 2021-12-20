# SETTINGS
from options import systemOptions

systemSettings = {
	'globalHpMaxCooficiant': 3.5,
	'globalXpMaxCooficiant': 0.8,
	'globalEpMaxCooficiant': 0.4,
	'globalMpMaxCooficiant': 0.3,

	'cmdCols': 70,
	'cmdLines': 50,
}


# GLOBAL VARS
defaultColor = 'wht'

invTypeKey = {
	'potion': 'potions',
	'weapon': 'weapons',
	'armor': 'armor',
	'shield': 'shields',
	'spell': 'spells',
	'keyItem': 'keyItems',
}

invTypeKeyReverse = {
	'potions': 'potion',
	'weapons': 'weapon',
	'armor': 'armor',
	'shields': 'shield',
	'spells': 'spell',
	'keyItems': 'keyItem',
}

invCatName = {
	'gold': 'Gold',
	'potions': 'Potions',
	'weapons': 'Weapons',
	'armor': 'Armor',
	'shields': 'Shields',
	'spells': 'Spells',
	'keyItems': 'Key Items',
}

# itmTierColor = {
#     1: 'wht_b',
#     2: 'grn_b',
#     3: 'blu_b',
#     4: 'mgt_b',
#     5: 'ylw_b',
# }

itmTierColor = {
    1: 'wht_b',
    2: 'blu_b',
    3: 'prp_b',
    4: 'red_b',
    5: 'ylw_b',
}

itmTierName = {
    1: 'Common',
    2: 'Rare',
    3: 'Super Rare',
    4: 'Exotic',
    5: 'Legendary',
}

itmTierSymbol = {
    1: 'C',
    2: 'R',
    3: 'S',
    4: 'E',
    5: 'L',
}


# COLORS
if systemOptions['debug']['pcMode'] == True:
	textColor = {
		'blk': '\u001b[30m',
		'red': '\u001b[31m',
		'org': '\u001b[38;5;202m',
		'grn': '\u001b[32m',
		'ylw': '\u001b[33m',
		'blu': '\u001b[34m',
		'mgt': '\u001b[35m',
		'cya': '\u001b[36m',
		'wht': '\u001b[37;0m',
		'blk_b': '\u001b[30;1m',
		'red_b': '\u001b[38;5;196;1m',
		'org_b': '\u001b[38;5;202m',
		'grn_b': '\u001b[38;5;82;1m',
		'ylw_b': '\u001b[38;5;214;1m',
		'blu_b': '\u001b[38;5;75;1m',
		'blu_2': '\u001b[38;5;81m',
		'mgt_b': '\u001b[38;5;201;1m',
		'prp_b': '\u001b[38;5;129;1m',
		'cya_b': '\u001b[38;5;51;1m',
		'wht_b': '\u001b[37;1m',
		'gry_b': '\u001b[38;5;250m',
		'gol_b': '\u001b[38;5;220m',
		'reset': '\u001b[0m',
		}
else: 
	textColor = {
		'blk': '',
		'red': '',
		'org': '',
		'grn': '',
		'ylw': '',
		'blu': '',
		'mgt': '',
		'cya': '',
		'wht': '',
		'blk_b': '',
		'red_b': '',
		'org_b': '',
		'grn_b': '',
		'ylw_b': '',
		'blu_b': '',
		'blu_2': '',
		'mgt_b': '',
		'prp_b': '',
		'cya_b': '',
		'wht_b': '',
		'gry_b': '',
		'gol_b': '',
		'reset': '',
	}
		
