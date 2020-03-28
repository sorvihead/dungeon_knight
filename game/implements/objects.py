from typing import List, Iterator

from game.interfaces.abstract_objects import AbstractObject
from game.interfaces.abstract_objects import Creature
from game.interfaces.abstract_objects import Interactive
from game.models.stats import Stats


class Hero(Creature):
    def __init__(self, icon, stats: Stats, position: List[int]):
        self._level = 1
        self._exp = 0
        self._gold = 0
        super(Hero, self).__init__(icon, stats, position)

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, level: int):
        self._level = level

    @property
    def exp(self) -> int:
        return self._exp

    @exp.setter
    def exp(self, exp: int):
        self._exp = exp

    @property
    def gold(self) -> int:
        return self._gold

    @gold.setter
    def gold(self, gold: int):
        self._gold = gold

    def level_up(self) -> Iterator[List[str]]:
        while self._exp >= 100 * (2 ** (self._level - 1)):
            yield "Level up"
            self._level += 1
            self._stats.strength += 2
            self._stats.endurance += 2
            self._hero_points.mp = self.hero_points.calc_max_mp(self.stats.intelligence)
            self._hero_points.hp = self.hero_points.calc_max_hp(self.stats.endurance)


class Enemy(Creature, Interactive):
    def __init__(self, icon, stats: Stats, xp: int, position: List[int]):
        self._xp = xp
        super(Enemy, self).__init__(icon, stats, position)  # FIXME

    def interact(self, engine, hero):
        pass  # FIXME


class Ally(AbstractObject, Interactive):
    def __init__(self, icon, action, position: List[int]):
        self._icon = icon
        self._action = action
        self._position = position

    def draw(self, display):
        pass  # FIXME

    def interact(self, engine, hero):
        pass  # FIXME
