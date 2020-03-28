from game.interfaces.abstract_effects import AbstractEffect


class Berserk(AbstractEffect):
    duration = 1.0

    def apply_effect(self):
        stats = dict(
            strength=self.stats.strength + 7,
            endurance=self.stats.endurance + 7,
            agility=self.stats.agility + 7,
            luck=self.stats.luck + 7,
            perception=self.stats.perception - 3,
            charisma=self.stats.charisma - 3,
            intelligence=self.stats.intelligence - 3
        )
        self.change_stats(**stats)
        # self._positive_effects.append(self)

    def cancel_effects(self, curr_time: float) -> AbstractEffect:
        if (curr_time - self._start_time) >= self.duration:
            print("Отменяю Берсерка")
            return self._base
        else:
            print("Спускаюсь вниз от берсерка")
            new_base = super(Berserk, self).cancel_effects(curr_time)
            if new_base:
                self.__init__(new_base, self._start_time)
            return self


class Blessing(AbstractEffect):
    duration = 2.0

    def apply_effect(self):
        stats = dict(
            strength=self.stats.strength + 2,
            endurance=self.stats.endurance + 2,
            agility=self.stats.agility + 2,
            luck=self.stats.luck + 2,
            perception=self.stats.perception + 2,
            charisma=self.stats.charisma + 2,
            intelligence=self.stats.intelligence + 2
        )
        self.change_stats(**stats)
        # self._positive_effects.append(self)

    def cancel_effects(self, curr_time: float) -> AbstractEffect:
        if (curr_time - self._start_time) >= self.duration:
            print("Отменяю блессинг")
            return self._base
        else:
            print("Спускаюсь вниз от блессинга")
            new_base = super(Blessing, self).cancel_effects(curr_time)
            if new_base:
                self.__init__(new_base, self._start_time)
            return self


class Weakness(AbstractEffect):
    duration = 3.0

    def apply_effect(self):
        stats = dict(
            strength=self.stats.strength - 4,
            endurance=self.stats.endurance - 4,
            agility=self.stats.agility - 4
        )
        self.change_stats(**stats)
        # self._negative_effects.append(self)

    def cancel_effects(self, curr_time: float) -> AbstractEffect:
        if (curr_time - self._start_time) >= self.duration:
            print("Отменяю викнесс")
            return self._base
        else:
            print("Спускаюсь вниз от викнесса")
            new_base = super(Weakness, self).cancel_effects(curr_time)
            if new_base:
                self.__init__(new_base, self._start_time)
            return self
