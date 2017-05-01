import collections

#enum
class Skill(object):
  HEAVY_SWING= 1
  MAIM = 2
  STORMS_EYE = 3
  STORMS_PATH = 4
  SKULL_SUNDER = 5
  BUTCHERS_BLOCK = 6
  FRACTURE = 7
  DEFIANCE = 8
  DELIVERANCE = 9
  BRUTAL_SWING = 10
  BERSERK = 11
  INFURIATE = 12
  RAW_INTUITION = 13
  INTERNAL_RELEASE = 14
  INNER_BEAST = 15
  UNCHAINED = 16
  STEEL_CYCLONE = 17
  FELL_CLEAVE = 18
  DECIMATE = 19
  SUPRAMAX_POTION_OF_STRENGTH_HQ = 20


skills = [
  {
    'id': Skill.HEAVY_SWING,
    'name': 'Heavy Swing',
    'xivdb': ['action', 31],
    'gcd': 1,
    'potency': 150,
  },
  {
    'id': Skill.MAIM,
    'name': 'Maim',
    'xivdb': ['action', 37],
    'gcd': 1,
    'potency': 100,
    'cpotency': 190,
  },
  {
    'id': Skill.STORMS_EYE,
    'name': "Storm's Eye",
    'xivdb': ['action', 45],
    'gcd': 1,
    'potency': 100,
    'cpotency': 200,
  },
  {
    'id': Skill.STORMS_PATH,
    'name': "Storm's Path",
    'xivdb': ['action', 42],
    'gcd': 1,
    'potency': 100,
    'cpotency': 250,
  },
  {
    'id': Skill.SKULL_SUNDER,
    'name': 'Skull Sunder',
    'xivdb': ['action', 35],
    'gcd': 1,
    'potency': 100,
    'cpotency': 200,
  },
  {
    'id': Skill.BUTCHERS_BLOCK,
    'name': "Butcher's Block",
    'xivdb': ['action', 47],
    'gcd': 1,
    'potency': 100,
    'cpotency': 280,
  },
  {
    'id': Skill.FRACTURE,
    'name': 'Fracture',
    'xivdb': ['action', 33],
    'gcd': 1,
    'potency': 100,
    'dotlength': 30,
    'dotpotency': 20,
  },
  {
    'id': Skill.DEFIANCE,
    'name': 'Defiance',
    'xivdb': ['action', 48],
    'gcd': 0,
  },
  {
    'id': Skill.DELIVERANCE,
    'name': 'Deliverance',
    'xivdb': ['action', 33],
    'gcd': 0,
  },
  {
    'id': Skill.BRUTAL_SWING,
    'name': 'Brutal Swing',
    'xivdb': ['action', 39],
    'gcd': 0,
    'potency': 100,
  },
  {
    'id': Skill.BERSERK,
    'name': 'Berserk',
    'xivdb': ['action', 38],
    'gcd': 0,
  },
  {
    'id': Skill.INFURIATE,
    'name': 'Infuriate',
    'xivdb': ['action', 52],
    'gcd': 0,
  },
  {
    'id': Skill.RAW_INTUITION,
    'name': 'Raw Intuition',
    'xivdb': ['action', 3551],
    'gcd': 0,
  },
  {
    'id': Skill.INTERNAL_RELEASE,
    'name': 'Internal Release',
    'xivdb': ['action', 59],
    'gcd': 0,
  },
  {
    'id': Skill.INNER_BEAST,
    'name': 'Inner Beast',
    'xivdb': ['action', 49],
    'gcd': 1,
    'potency': 300,
  },
  {
    'id': Skill.UNCHAINED,
    'name': 'Unchained',
    'xivdb': ['action', 50],
    'gcd': 0,
  },
  {
    'id': Skill.STEEL_CYCLONE,
    'name': 'Steel Cyclone',
    'xivdb': ['action', 51],
    'gcd': 1,
    'potency': 200,
  },
  {
    'id': Skill.FELL_CLEAVE,
    'name': 'Fell Cleave',
    'xivdb': ['action', 51],
    'gcd': 1,
    'potency': 500,
  },
  {
    'id': Skill.DECIMATE,
    'name': 'Decimate',
    'xivdb': ['action', 51],
    'gcd': 1,
    'potency': 280,
  },
  {
    'id': Skill.SUPRAMAX_POTION_OF_STRENGTH_HQ,
    'name': 'Supramax-Potion of Strength HQ',
    'xivdb': ['item', 16716],
    'gcd': 0,
  },
]

Action = collections.namedtuple('Action', 'id time')

timeline = [
  Action(1, 0.0),
  Action(2, 2.5),
  Action(3, 5.0),
  Action(1, 7.5),
  Action(5, 10.0),
  Action(6, 12.5),
]
