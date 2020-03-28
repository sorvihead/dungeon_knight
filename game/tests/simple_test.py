import time

from game.implements.effects import Berserk, Blessing, Weakness
from game.implements.objects import Hero
from game.models.stats import Stats

if __name__ == '__main__':
    s = Stats(
        strength=11,
        perception=7,
        endurance=7,
        charisma=8,
        intelligence=10,
        agility=9,
        luck=5
    )
    h = Hero(
        0, s, [1, 1]
    )
    print("Hero: ", h.stats)
    print(h.hero_points)
    b = Berserk(h, time.time())
    print("Berserk: ", b.stats)
    print(b.hero_points)
    bless = Blessing(b, time.time())
    print("Blessing: ", bless.stats)
    print(bless.hero_points)
    w = Weakness(bless, time.time())
    print("Weakness: ", w.stats)
    print(w.hero_points)
    # time.sleep(1)
    w = w.cancel_effects(time.time())
    print("Cancel Bereserk: ", w.stats)
    print(w.hero_points)
    time.sleep(1.5)
    w = w.cancel_effects(time.time())
    print("Cancel Blessing: ", w.stats)
    print(w.hero_points)
