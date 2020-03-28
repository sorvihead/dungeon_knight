from game.logic.game import Game
from game.models.stats import Stats

if __name__ == '__main__':

    stats = Stats(
        strength=1,
        perception=1,
        endurance=1,
        charisma=1,
        intelligence=1,
        agility=1,
        luck=1
    )
    g = Game(stats, 60)
    g.run()
