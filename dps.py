import collections
import math

#enum
class Skill(object):
  HEAVY_SWING = 1
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
  OVERPOWER = 34
  ONSLAUGHT = 35
  UPHEAVAL = 36
  INNER_RELEASE = 37
  EMBOLDEN = 38
  CHAIN_STRATAGEM = 39
  SPREAD_BALANCE = 40
  BATTLE_VOICE = 41

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
    'beast': 10,
  },
  {
    'id': Skill.STORMS_EYE,
    'name': "Storm's Eye",
    'xivdb': ['action', 45],
    'gcd': 1,
    'potency': 100,
    'cpotency': 270,
    'duration': 30,
    'beast': 10,
  },
  {
    'id': Skill.STORMS_PATH,
    'name': "Storm's Path",
    'xivdb': ['action', 42],
    'gcd': 1,
    'potency': 100,
    'cpotency': 250,
    'beast': 20,
  },
  {
    'id': Skill.SKULL_SUNDER,
    'name': 'Skull Sunder',
    'xivdb': ['action', 35],
    'gcd': 1,
    'potency': 100,
    'cpotency': 200,
    'beast': 20,
  },
  {
    'id': Skill.BUTCHERS_BLOCK,
    'name': "Butcher's Block",
    'xivdb': ['action', 47],
    'gcd': 1,
    'potency': 100,
    'cpotency': 280,
    'beast': 10,
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
    'beast': 50,
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
    'potency': 350,
    'beast': -50,
  },
  {
    'id': Skill.UNCHAINED,
    'name': 'Unchained',
    'xivdb': ['action', 50],
    'gcd': 0,
    'beast': -50,
  },
  {
    'id': Skill.STEEL_CYCLONE,
    'name': 'Steel Cyclone',
    'xivdb': ['action', 51],
    'gcd': 1,
    'potency': 200,
    'beast': -50,
  },
  {
    'id': Skill.FELL_CLEAVE,
    'name': 'Fell Cleave',
    'xivdb': ['action', 51],
    'gcd': 1,
    'potency': 500,
    'beast': -50,
  },
  {
    'id': Skill.DECIMATE,
    'name': 'Decimate',
    'xivdb': ['action', 51],
    'gcd': 1,
    'potency': 280,
    'beast': -50,
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
  {
    'id': Skill.OVERPOWER,
    'name': 'Overpower',
    'xivdb': ['action', 2188],
    'gcd': 1,
    'potency': 120,
  },
  {
    'id': Skill.ONSLAUGHT,
    'name': 'Onslaught',
    'gcd': 0,
    'potency': 100,
    'beast': -20,
  },
  {
    'id': Skill.UPHEAVAL,
    'name': 'Upheaval',
    'gcd': 0,
    'potency': 300,
    'beast': -30,
  },
  {
    'id': Skill.INNER_RELEASE,
    'name': 'Inner Release',
    'gcd': 0,
    'duration': 20,
    'beast': -20,
  },
  {
    'id': Skill.EMBOLDEN,
    'name': 'Embolden',
    'gcd': 0,
    'duration': 20,
  },
  {
    'id': Skill.CHAIN_STRATAGEM,
    'name': 'Chain Stratagem',
    'gcd': 0,
    'duration': 15,
  },
  {
    'id': Skill.SPREAD_BALANCE,
    'name': 'Balance (spread)',
    'gcd': 0,
    'duration': 30,
  },
  {
    'id': Skill.BATTLE_VOICE,
    'name': 'Battle Voice',
    'xivdb': ['action', 118],
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

  def gcd_time(self):
    # TODO calculate this from ss for reals
    return 2.5

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

  def time_remaining(self, id, time):
    if not id in self._effects:
      return 0
    end_time = self._effects[id]
    if end_time is None:
      return 1000000 # "infinity"
    return end_time - time


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


Damage = collections.namedtuple('Damage', 'id damage crit_chance crit_sev pot mult')
DotDamage = collections.namedtuple('DotDamage', 'id damage crit_chance crit_sev begin end pot')


class WarriorState(object):
  ignores_defiance = [
    Skill.FELL_CLEAVE,
    Skill.DECIMATE,
    Skill.UNCHAINED,
    Skill.INNER_BEAST,
    Skill.STEEL_CYCLONE
  ]
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
  infuriate_reducers = warrior_combo_ignore

  def __init__(self, character):
    self.character = character
    self.beast = 0
    self.status = StatusEffects()

    self.combo = ComboTracker(self.warrior_combos, self.warrior_combo_ignore)

  def crit_chance(self, time):
    crit_chance = self.character.crit_chance()
    # 10% chance at 100 beast
    if self.status.has_effect(Skill.DELIVERANCE, time):
      crit_chance += 0.001 * self.beast
    if self.status.has_effect(Skill.BATTLE_LITANY, time):
      crit_chance += 0.15
    if self.status.has_effect(Skill.CHAIN_STRATAGEM, time):
      crit_chance += 0.2
    return crit_chance

  # Returns direct and dot and crit info so that the caller can calculate
  # ranges or averages as needed.
  def apply_skill_and_get_damage(self, id, time):
    crit_chance = self.crit_chance(time)
    crit_sev = self.character.crit_severity()

    direct_damage = None

    if 'potency' in skills[id]:
      potency = (skills[id]['cpotency']
          if self.combo.would_continue_combo(id) else skills[id]['potency'])
      mult = self.get_multiplier(time)
      damage = self.character.potency_to_damage(potency * mult)
      direct_damage = Damage(id, damage, crit_chance, crit_sev, potency, mult)

    self.apply_skill(id, time)
    return direct_damage, []

  def finish_fight(self, time):
    final = []
    return None, final

  def get_multiplier(self, time):
    mult = 1.0
    if self.status.has_effect(Skill.BERSERK, time):
      mult *= 1.5
    if self.status.has_effect(Skill.STORMS_EYE, time):
      mult *= 1.2
    if self.status.has_effect(Skill.DELIVERANCE, time):
      mult *= 1.05
    elif self.status.has_effect(Skill.DEFIANCE, time):
      if not self.status.has_effect(Skill.UNCHAINED, time):
        if id not in ignores_defiance:
          mult *= 0.75

    # TODO really should be on the mob and not on self.status
    # TODO 10% slashing resistance != 10% damage increase but nobody seems
    # to have a good formula for this.  Sad trombone noise.
    # TODO Separate out skills and effects.  For now MAIM=slashing <_<
    if self.status.has_effect(Skill.MAIM, time):
      mult *= 1.1
    if self.status.has_effect(Skill.TRICK_ATTACK, time):
      mult *= 1.1
    if self.status.has_effect(Skill.HYPERCHARGE, time):
      mult *= 1.05
    embolden_time = self.status.time_remaining(Skill.EMBOLDEN, time)
    if embolden_time > 0:
      mult *= 1 + 0.02 * math.ceil(embolden_time / 4.0)

    if self.status.has_effect(Skill.SPREAD_BALANCE, time):
      mult *= 1.1
    # Battle voice increases "direct hit rate" (affects tanks? probably no?)
    # Potion affects stats, not a flat mult
    # Fey wind affects skill speed
    return mult

  def apply_skill(self, id, time):
    if 'beast' in skills[id]:
      beast = skills[id]['beast']
      # inner release halves skills that cost beast gauge
      if beast < 0:
        if self.status.has_effect(Skill.INNER_RELEASE, time):
          beast = math.floor(beast / 2)
      assert(self.beast + beast >= 0)
      self.beast = max(min(self.beast + beast, 100), 0)

    if skills[id]['gcd']:
      is_combo = self.combo.apply_skill(id)
      if 'duration' in skills[id]:
        self.status.add_effect(id, time, skills[id]['duration'])
    else:
      if id in [Skill.DELIVERANCE, Skill.DEFIANCE]:
        if self.status.has_effect(id, time):
          self.status.remove_effect(id)
          self.beast = 0
        else:
          if id == Skill.DELIVERANCE:
            self.status.remove_effect(Skill.DEFIANCE)
          else:
            self.status.remove_effect(Skill.DELIVERANCE)
          self.status.add_effect(id, time, None)
          self.beast = math.floor(self.beast / 2)
      elif 'duration' in skills[id]:
        self.status.add_effect(id, time, skills[id]['duration'])


class PotencyCalculator(object):
  def __init__(self, state):
    self.state = state
    self.damage = 0

  @staticmethod
  def average_direct(direct):
    avg = (direct.damage * direct.crit_chance * direct.crit_sev +
           (1 - direct.crit_chance) * direct.damage)
    return avg

  @staticmethod
  def average_dot(dot):
    per_tick_avg = (dot.damage * dot.crit_chance * dot.crit_sev +
                    (1 - dot.crit_chance) * dot.damage)
    ticks = (dot.end - dot.begin) / 3
    return per_tick_avg * ticks

  def process_damage(self, direct, dots):
    if dots:
      for dot in dots:
        avg = PotencyCalculator.average_dot(dot)
        print "damage: %s: %d (dot)" % (skills[dot.id]['name'], avg)
        self.damage += avg
    if direct:
      avg = PotencyCalculator.average_direct(direct)
      print "damage: %s: %d" % (skills[direct.id]['name'], avg)
      self.damage += avg

  def handle(self, id, time):
    direct, dots = self.state.apply_skill_and_get_damage(id, time)
    self.process_damage(direct, dots)
    return direct

  def finish_fight(self, time):
    direct, dots = self.state.finish_fight(time)
    self.process_damage(direct, dots)


class WarriorHeuristic(object):
  def __init__(self, character, state, start_time):
    self.character = character
    self.state = state
    self.status = state.status
    self.next_gcd = start_time
    self.combo = []

  def next_gcd_time(self):
    return self.next_gcd

  def next_action(self):
    time = self.next_gcd
    self.next_gcd += self.character.gcd_time()

    storms_eye_combo = [ Skill.STORMS_EYE, Skill.MAIM, Skill.HEAVY_SWING ]
    bb_combo = [ Skill.BUTCHERS_BLOCK, Skill.SKULL_SUNDER, Skill.HEAVY_SWING ]

    maim_gcds = self.status.time_remaining(Skill.MAIM, time) / self.character.gcd_time()
    eye_gcds = self.status.time_remaining(Skill.STORMS_EYE, time) / self.character.gcd_time()

    # TODO technically need animation time in here too
    if maim_gcds <= 2:
      if len(self.combo) == 0 or not Skill.MAIM in self.combo:
        self.combo = storms_eye_combo

    if len(self.combo):
      if self.state.beast >= 90:
        return Action(Skill.FELL_CLEAVE, time)
      return Action(self.combo.pop(), time)

    if eye_gcds <= 4:
      self.combo = storms_eye_combo
      return Action(self.combo.pop(), time)

    if eye_gcds <= 4:
      self.combo = storms_eye_combo
    else:
      self.combo = bb_combo
    return Action(self.combo.pop(), time)

#embolden 16s
#trick attack 11s
#litany 5s?? A
#chain strategem 15s

def main():
  character = Character(85, 1590, 682, 1193)
  state = WarriorState(character)
  heuristic = WarriorHeuristic(character, state, 0)

  x = PotencyCalculator(state)
  x.handle(Skill.DELIVERANCE, -10)

  while True:
    n = heuristic.next_action()
    if n.time > 90:
      break

    mult = state.get_multiplier(n.time)
    damage = x.handle(n.id, n.time)

    debug = {}
    debug['beast'] = state.beast
    debug['effect_maim'] = state.status.time_remaining(Skill.MAIM, n.time)
    debug['effect_eye'] = state.status.time_remaining(Skill.STORMS_EYE, n.time)
    debug['skill'] = skills[n.id]['name']
    debug['time'] = n.time
    debug['damage'] = PotencyCalculator.average_direct(damage)
    debug['potency'] = damage.pot
    debug['mult'] = mult
    debug['crit_chance'] = damage.crit_chance
    debug['crit_chance'] = damage.crit_sev

    print debug
  x.finish_fight(90)

  print 'damage: %d' % x.damage

if __name__ == '__main__':
  main()
