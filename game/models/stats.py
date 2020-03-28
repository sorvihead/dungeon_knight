from dataclasses import dataclass


@dataclass
class Stats:
    strength: int
    perception: int
    endurance: int
    charisma: int
    intelligence: int
    agility: int
    luck: int

    def change(self, **kwargs):
        if all(key in self.__dict__.keys() for key in kwargs.keys()):
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
        else:
            raise KeyError

    def __copy__(self):
        return Stats(
            strength=self.strength,
            perception=self.perception,
            endurance=self.endurance,
            charisma=self.charisma,
            intelligence=self.intelligence,
            agility=self.agility,
            luck=self.luck
        )

    def copy(self):
        return self.__copy__()
