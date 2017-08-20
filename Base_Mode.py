# -*- coding: UTF-8 -*-


class Person(object):
    def __init__(self):
        self.name = 'player'
        # Character attribute
        self.strength = 10
        self.endurance = 10
        self.dexterity = 10
        self.intellect = 10
        self.luck = 10

        # Base attribute
        self.level = 1
        self.experience = 0
        self.life = 100
        self.mana = 100
        self.attack = 10
        self.defense = 10


class Monster(object):
    def __init__(self):
        self.name = 'monter'

        self.life = 100
        self.attack = 5
        self.defense = 5


class Armor(object):
    def __init__(self):
        pass
