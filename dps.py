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
  TOMAHAWK = 20
  SUPRAMAX_POTION_OF_STRENGTH_HQ = 21


skill_list = [
  {
    'id': Skill.HEAVY_SWING,
    'name': 'Heavy Swing',
    'xivdb': ['action', 31],
    'gcd': 1,
    'potency': 150,
    'cpotency': 150,
  },
  {
    'id': Skill.MAIM,
    'name': 'Maim',
    'xivdb': ['action', 37],
    'gcd': 1,
    'potency': 100,
    'cpotency': 190,
    'eduration': 24,
  },
  {
    'id': Skill.STORMS_EYE,
    'name': "Storm's Eye",
    'xivdb': ['action', 45],
    'gcd': 1,
    'potency': 100,
    'cpotency': 270,
    'eduration': 20,
  },
  {
    'id': Skill.STORMS_PATH,
    'name': "Storm's Path",
    'xivdb': ['action', 42],
    'gcd': 1,
    'potency': 100,
    'cpotency': 250,
    'eduration': 20,
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
    'id': Skill.TOMAHAWK,
    'name': 'Tomahawk',
    'xivdb': ['action', 46],
    'gcd': 1,
    'potency': 130,
  },
  {
    'id': Skill.SUPRAMAX_POTION_OF_STRENGTH_HQ,
    'name': 'Supramax-Potion of Strength HQ',
    'xivdb': ['item', 16716],
    'gcd': 0,
  },
]

skills = dict((x['id'], x) for x in skill_list)

Action = collections.namedtuple('Action', 'id time')

timeline = [
  Action(1, 0.0),
  Action(2, 2.5),
  Action(3, 5.0),
  Action(1, 7.5),
  Action(5, 10.0),
  Action(6, 12.5),
]

# Track currently active
class StatusEffects(object):
  def __init__(self):
    # map of skill id => ending time (none for infinity)
    _effects = {}

  def add_effect(self, id, time, dur):
    pass

  def has_effect(self, id, time):
    if not id in _effects:
      return False


# Combo tracker is a graph where every transition goes to the state
# of the same type (i.e. transition X from all nodes goes to node X).
# The None node is the starting node not in the middle of any combo.
# It's assumed that a combo can be started in the middle of any other
# combo, i.e. that the first action in a combo chain is a valid
# transition from all nodes.  This all supports a set of "ignore"
# actions that do not break the combo but are also not considered
# part of a combo.  Any other action will break the combo and reset
# the current node to the None state.
class ComboTracker(object):
  def __init__(self, combos, ignore):
    self.combos = combos
    self.ignore = ignore
    self.current_node = None

    # Assume all states allow to go to a starter
    starters = set([x[0] for x in combos])

    Node = collections.namedtuple('Node', 'id trans')
    self.graph = dict((x, Node(x, list(starters))) for x in starters)
    self.graph[None] = Node(None, list(starters))

    for chain in combos:
      for i in range(1, len(chain)):
        action = chain[i]
        if not action in self.graph:
          self.graph[action] = Node(action, list(starters))
        self.graph[chain[i - 1]].trans.append(action)

  # returns true if this skill is part of a combo
  def apply_skill(self, id):
    node = self.graph[self.current_node]
    if id in node.trans:
      # combo continues on the chain
      self.current_node = id
      return True
    if id in self.ignore:
      # combo not broken, but not part of a combo
      return False
    # combo broken
    self.current_node = None
    return False

  def would_continue_combo(self, id):
    return id in self.graph[self.current_node].trans


class WarriorState(object):
  def __init__(self):
    self.stacks = 0
    self.status = StatusEffects()

    warrior_combos = [
      [ Skill.HEAVY_SWING, Skill.MAIM, Skill.STORMS_EYE ],
      [ Skill.HEAVY_SWING, Skill.MAIM, Skill.STORMS_PATH ],
      [ Skill.HEAVY_SWING, Skill.SKULL_SUNDER, Skill.BUTCHERS_BLOCK ],
    ]
    warrior_combo_ignore = [
      Skill.INNER_BEAST,
      Skill.STEEL_CYCLONE,
      Skill.FELL_CLEAVE,
      Skill.DECIMATE,
    ]
    self.combo = ComboTracker(warrior_combos, warrior_combo_ignore)

  def apply_skill_and_get_damage(self, id, time):
    damage = self.get_damage(id, time)
    print "damage: %d: %d" % (id, damage)
    self.apply_skill(id, time)
    return damage

  def get_damage(self, id, time):
    # TODO combo needs to keep track of time too
    if self.combo.would_continue_combo(id):
      return skills[id]['cpotency']
    return skills[id]['potency']

  def apply_skill(self, id, time):
    is_combo = self.combo.apply_skill(id)
    if is_combo:
      if id == Skill.MAIM:
        self.status.add_effect(Skill.MAIM, time,
            skills[Skill.MAIM]['eduration'])
      if id == Skill.STORMS_EYE:
        self.status.add_effect(Skill.MAIM, time,
            skills[Skill.STORMS_EYE]['eduration'])
      if id == Skill.STORMS_PATH:
        self.status.add_effect(Skill.MAIM, time,
            skills[Skill.STORMS_PATH]['eduration'])


class PotencyCalculator(object):
  def __init__(self, timeline):
    self.timeline = timeline

  def calculate(self):
    state = WarriorState()
    damage = 0
    for action in self.timeline:
      # TODO: need to account for animation delay
      id = action.id
      time = action.time

      # TODO: add dot damage here too? Or at the end??
      damage += state.apply_skill_and_get_damage(id, time)
    return damage


def main():
  x = PotencyCalculator(timeline)
  print 'damage: %d' % x.calculate()

if __name__ == '__main__':
  main()
