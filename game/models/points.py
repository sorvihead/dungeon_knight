from dataclasses import dataclass

from game.models.stats import Stats


@dataclass
class HeroPoints:
    curr_hp: int
    curr_mp: int
    max_hp: int
    max_mp: int

    @classmethod
    def from_stats(cls, stats: Stats):
        hp = cls.calc_max_hp(stats.endurance)
        mp = cls.calc_max_mp(stats.intelligence)
        return cls(hp, mp, hp, mp)

    def change(self, stats: Stats):
        old_max_hp = self.max_hp
        self.max_hp = self.calc_max_hp(stats.endurance)
        self.curr_hp += self.max_hp - old_max_hp
        old_max_mp = self.max_mp
        self.max_mp = self.calc_max_mp(stats.intelligence)
        self.curr_mp += self.max_mp - old_max_mp

    @staticmethod
    def calc_max_hp(endurance: int) -> int:
        return 5 + endurance * 2

    @staticmethod
    def calc_max_mp(intelligence: int) -> int:
        return 4 + intelligence * 2

    def __copy__(self):
        return HeroPoints(
            self.curr_hp, self.curr_mp, self.max_hp, self.max_mp
        )

    def copy(self):
        return self.__copy__()
