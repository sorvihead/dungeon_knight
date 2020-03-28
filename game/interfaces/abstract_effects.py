import time
from abc import ABCMeta, abstractmethod

from game.implements.objects import Hero


class AbstractEffect(Hero, metaclass=ABCMeta):
    def __init__(self, base: Hero, start_time: float):
        self._base = base
        super(AbstractEffect, self).__init__(self._base.icon, self._base.stats, self._base.position)
        self._start_time = start_time
        self.apply_effect()

    @abstractmethod
    def apply_effect(self):
        pass

    def cancel_effects(self, curr_time: float):
        if isinstance(self._base, AbstractEffect):
            return self._base.cancel_effects(curr_time)
