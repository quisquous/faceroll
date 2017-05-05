import collections
import math

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
  VENGEANCE = 21
  SUPRAMAX_POTION_OF_STRENGTH_HQ = 30
  TRICK_ATTACK = 31
  HYPERCHARGE = 32
  BATTLE_LITANY = 33


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
    'duration': 24,
  },
  {
    'id': Skill.STORMS_EYE,
    'name': "Storm's Eye",
    'xivdb': ['action', 45],
    'gcd': 1,
    'potency': 100,
    'cpotency': 270,
    'duration': 20,
  },
  {
    'id': Skill.STORMS_PATH,
    'name': "Storm's Path",
    'xivdb': ['action', 42],
    'gcd': 1,
    'potency': 100,
    'cpotency': 250,
    'duration': 20,
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
    'duration': 30,
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
    'duration': 20,
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
    'duration': 15,
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
    'id': Skill.VENGEANCE,
    'name': 'Vengeance',
    'xivdb': ['action', 44],
    'gcd': 0,
    'duration': 15,
  },
  {
    'id': Skill.SUPRAMAX_POTION_OF_STRENGTH_HQ,
    'name': 'Supramax-Potion of Strength HQ',
    'xivdb': ['item', 16716],
    'gcd': 0,
  },
  {
    'id': Skill.TRICK_ATTACK,
    'name': 'Trick Attack',
    'xivdb': ['action', 2258],
    'gcd': 0,
    'duration': 10,
  },
  {
    # TODO This isn't really a skill.
    'id': Skill.HYPERCHARGE,
    'name': 'Hypercharge',
    'xivdb': ['action', 2885],
    'gcd': 0,
    'duration': 20,
  },
  {
    'id': Skill.BATTLE_LITANY,
    'name': 'Battle Litany',
    'xivdb': ['action', 3557],
    'gcd': 0,
    'duration': 20,
  },
]

skills = dict((x['id'], x) for x in skill_list)


Action = collections.namedtuple('Action', 'id time')


# From http://www.eonet.ne.jp/~versatile/ku-so/ff14dps.html
# From https://dervyxiv.wordpress.com/damage-formulae-other-mechanics/
class Character(object):
  def __init__(self, weapon_damage, attack_power, determination, crit):
    self.weapon_damage = weapon_damage
    self.attack_power = attack_power
    self.determination = determination
    self.crit = crit
    # TODO hardcoded for warrior oops
    self.job_modifier = 20.9

  def potency_to_damage(self, potency):
    # TODO this will need to be refigured to include potions
    wep = (self.job_modifier + self.weapon_damage) * 0.00458
    det = (self.determination - 218) * 0.000137 + 1
    return wep * det * self.attack_power * potency / 100

  def crit_chance(self):
    return (self.crit - 354.0) / (858.0 * 5.0) + 0.05

  def crit_severity(self):
    return (self.crit - 354.0) / (858.0 * 5.0) + 1.45


# Track currently active effects.
# TODO probably need one of these per target (and self)
class StatusEffects(object):
  def __init__(self):
    # map of skill id => ending time (none for infinity)
    self._effects = {}

  def add_effect(self, id, time, dur):
    # TODO not all effects replace
    # TODO some effects collide
    if dur is None:
      self._effects[id] = None
    else:
      self._effects[id] = time + dur

  def remove_effect(self, id):
    if id in self._effects:
      self._effects.pop(id)

  def has_effect(self, id, time):
    if not id in self._effects:
      return False
    end_time = self._effects[id]
    if end_time is None:
      return True
    return time <= end_time


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

  # TODO combo needs to keep track of time too
  def would_continue_combo(self, id):
    return id in self.graph[self.current_node].trans


Damage = collections.namedtuple('Damage', 'damage crit_chance crit_sev')


class WarriorState(object):
  stack_users = [
    Skill.FELL_CLEAVE,
    Skill.DECIMATE,
    Skill.UNCHAINED,
    Skill.INNER_BEAST,
    Skill.STEEL_CYCLONE
  ]
  ignores_defiance = stack_users
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

  def __init__(self, character):
    self.character = character
    self.stacks = 0
    self.status = StatusEffects()

    self.combo = ComboTracker(self.warrior_combos, self.warrior_combo_ignore)

  def crit_chance(self, time):
    crit_chance = self.character.crit_chance()
    if self.status.has_effect(Skill.INTERNAL_RELEASE, time):
      crit_chance += 0.1
    if self.status.has_effect(Skill.DELIVERANCE, time):
      crit_chance += 0.02 * self.stacks
    if self.status.has_effect(Skill.BATTLE_LITANY, time):
      crit_chance += 0.15
    return crit_chance

  # Returns direct and dot and crit info so that the caller can calculate
  # ranges or averages as needed.
  def apply_skill_and_get_damage(self, id, time):
    crit_chance = self.crit_chance(time)
    crit_sev = self.character.crit_severity()

    direct_damage = None
    dot_damage = None

    if 'potency' in skills[id]:
      potency = (skills[id]['cpotency']
          if self.combo.would_continue_combo(id) else skills[id]['potency'])
      damage = self.get_damage(potency, time)
      direct_damage = Damage(damage, crit_chance, crit_sev)
    # TODO fracture shouldn't take into account slashing debuff
    # TODO dot potency should take into account skill speed
    if 'dotpotency' in skills[id]:
      damage = self.get_damage(skills[id]['dotpotency'], time)
      dot_damage = Damage(damage, crit_chance, crit_sev)

    self.apply_skill(id, time)
    return direct_damage, dot_damage

  def get_damage(self, potency, time):
    damage = self.character.potency_to_damage(potency)
    if self.status.has_effect(Skill.MAIM, time):
      damage *= 1.2
    if self.status.has_effect(Skill.BERSERK, time):
      damage *= 1.5
    if self.status.has_effect(Skill.DELIVERANCE, time):
      damage *= 1.05
    elif self.status.has_effect(Skill.DEFIANCE, time):
      if not self.status.has_effect(Skill.UNCHAINED, time):
        if id not in ignores_defiance:
          damage *= 0.75

    # TODO really should be on the mob and not on self.status
    # TODO 10% slashing resistance != 10% damage increase but nobody seems
    # to have a good formula for this.  Sad trombone noise.
    if self.status.has_effect(Skill.STORMS_EYE, time):
      damage *= 1.1
    if self.status.has_effect(Skill.TRICK_ATTACK, time):
      damage *= 1.1
    if self.status.has_effect(Skill.HYPERCHARGE, time):
      damage *= 1.1

    return damage

  def apply_skill(self, id, time):
    if skills[id]['gcd']:
      if id in self.stack_users:
        self.stacks = 0
      is_combo = self.combo.apply_skill(id)
      if not is_combo:
        return

      if id != Skill.HEAVY_SWING:
        self.stacks += 1

      if 'duration' in skills[id]:
        self.status.add_effect(id, time, skills[id]['duration'])
    else:
      if id in [Skill.RAW_INTUITION, Skill.VENGEANCE, Skill.BERSERK]:
        self.stacks += 1
      elif id == Skill.INFURIATE:
        self.stacks = 5

      if id in [Skill.DELIVERANCE, Skill.DEFIANCE]:
        if self.status.has_effect(id, time):
          self.status.remove_effect(id)
        else:
          if id == Skill.DELIVERANCE:
            self.status.remove_effect(Skill.DEFIANCE)
          else:
            self.status.remove_effect(Skill.DELIVERANCE)
          self.status.add_effect(id, time, None)
      elif 'duration' in skills[id]:
        self.status.add_effect(id, time, skills[id]['duration'])
    self.stacks = min(self.stacks, 5)


class PotencyCalculator(object):
  def __init__(self, timeline, character):
    self.timeline = timeline
    self.character = character

  def calculate(self):
    state = WarriorState(self.character)
    damage = 0
    for action in self.timeline:
      # TODO: need to account for animation delay
      id = action.id
      time = action.time

      direct, dot = state.apply_skill_and_get_damage(id, time)
      if direct:
        avg = (direct.damage * direct.crit_chance * direct.crit_sev +
               (1 - direct.crit_chance) * direct.damage)
        damage += avg
        print "damage: %s: %d" % (skills[id]['name'], avg)
      if dot:
        assert('duration' in skills[id])
        duration = skills[id]['duration']
        assert(math.floor(duration) == duration)
        assert(duration % 3 == 0)
        ticks = duration / 3

        # TODO dot damage should tick over time
        per_tick_avg = (dot.damage * dot.crit_chance * dot.crit_sev +
                        (1 - dot.crit_chance) * dot.damage)
        avg = per_tick_avg * ticks
        damage += avg
        print "damage: %s: %d (dot)" % (skills[id]['name'], avg)

    return damage


def main():
  character = Character(85, 1590, 682, 1193)

  timeline = [
    Action(Skill.DELIVERANCE, -10),
    Action(Skill.HEAVY_SWING, 0.0),
    Action(Skill.MAIM, 2.5),
    Action(Skill.STORMS_EYE, 5.0),
    Action(Skill.HEAVY_SWING, 7.5),
    Action(Skill.SKULL_SUNDER, 10.0),
    Action(Skill.BUTCHERS_BLOCK, 12.5),
    Action(Skill.FRACTURE, 15),
  ]

  x = PotencyCalculator(timeline, character)
  print 'damage: %d' % x.calculate()

if __name__ == '__main__':
  main()
