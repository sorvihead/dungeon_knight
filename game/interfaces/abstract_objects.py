from abc import ABCMeta, abstractmethod
from typing import List

from game.models.points import HeroPoints
from game.models.stats import Stats


class AbstractObject(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, display):
        pass


class Interactive(metaclass=ABCMeta):

    @abstractmethod
    def interact(self, engine, hero):
        pass


class Creature(AbstractObject):
    def __init__(self, icon, stats: Stats, position: List[int]):
        self._icon = icon
        self._stats = stats
        self._position = position
        self._hero_points = HeroPoints.from_stats(stats)
        self._positive_effects = []
        self._negative_effects = []

    def change_stats(self, **kwargs):
        self._stats.change(**kwargs)
        self._hero_points.change(self._stats)

    def draw(self, display):
        pass

    @property
    def hero_points(self) -> HeroPoints:
        return self._hero_points.copy()

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon):
        self._icon = icon

    @property
    def stats(self) -> Stats:
        return self._stats.copy()

    @property
    def position(self) -> List[int]:
        return self._position.copy()

    @position.setter
    def position(self, position: List[int]):
        self._position = position
