# -*- coding: UTF-8 -*-

__author__ = 'AllenG_G'

import os
import sys
import time
import pygame
import threading
import Base_Mode
from PyQt4 import QtGui
from PyQt4 import QtCore


class Model(object):
    def __init__(self):
        pass


class Controller(object):
    def __init__(self, model):
        pass


class MainUI(QtGui.QDialog):
    def __init__(self, model, controller):
        super(MainUI, self).__init__()
        self.setWindowTitle('BoringGame')

        self.mainLayout = QtGui.QHBoxLayout(self)

        self.playerPropertyLayout = QtGui.QVBoxLayout()
        self.monsterPropertyLayout = QtGui.QVBoxLayout()
        self.combatViewLayout = QtGui.QVBoxLayout()

        layout_gird_player = QtGui.QGridLayout()
        self.label_name = QtGui.QLabel('Name: ')
        self.player_name = QtGui.QLabel()
        self.label_level = QtGui.QLabel('Level: ')
        self.player_level = QtGui.QLabel()
        self.label_strength = QtGui.QLabel('Strength: ')
        self.player_strength = QtGui.QLabel()
        self.label_endurance = QtGui.QLabel('Endurance: ')
        self.player_endurance = QtGui.QLabel()
        self.label_dexterity = QtGui.QLabel('Dexterity: ')
        self.player_dexterity = QtGui.QLabel()
        self.label_intellect = QtGui.QLabel('Intellect: ')
        self.player_intellect = QtGui.QLabel()
        self.label_life = QtGui.QLabel('Life')
        self.player_life = QtGui.QLabel()
        self.label_attack = QtGui.QLabel('Attack')
        self.player_attack = QtGui.QLabel()
        self.label_defense = QtGui.QLabel('Defense')
        self.player_defense = QtGui.QLabel()

        layout_gird_player.addWidget(self.label_name, 0, 0)
        layout_gird_player.addWidget(self.player_name, 0, 1)
        layout_gird_player.addWidget(self.label_level, 1, 0)
        layout_gird_player.addWidget(self.player_level, 1, 1)
        layout_gird_player.addWidget(self.label_strength, 2, 0)
        layout_gird_player.addWidget(self.player_strength, 2, 1)
        layout_gird_player.addWidget(self.label_endurance, 3, 0)
        layout_gird_player.addWidget(self.player_endurance, 3, 1)
        layout_gird_player.addWidget(self.label_dexterity, 4, 0)
        layout_gird_player.addWidget(self.player_dexterity, 4, 1)
        layout_gird_player.addWidget(self.label_intellect, 5, 0)
        layout_gird_player.addWidget(self.player_intellect, 5, 1)
        layout_gird_player.addWidget(self.label_life, 6, 0)
        layout_gird_player.addWidget(self.player_life, 6, 1)
        layout_gird_player.addWidget(self.label_attack, 7, 0)
        layout_gird_player.addWidget(self.player_attack, 7, 1)
        layout_gird_player.addWidget(self.label_defense, 8, 0)
        layout_gird_player.addWidget(self.player_defense, 8, 1)

        layout_gird_monster = QtGui.QGridLayout()
        self.monster_name = QtGui.QLabel()
        self.monster_life = QtGui.QLabel()
        self.monster_attack = QtGui.QLabel()
        self.monster_defense = QtGui.QLabel()

        layout_gird_monster.addWidget(self.label_name, 0, 0)
        layout_gird_monster.addWidget(self.monster_name, 0, 1)
        layout_gird_monster.addWidget(self.label_life, 1, 0)
        layout_gird_monster.addWidget(self.monster_life, 1, 1)
        layout_gird_monster.addWidget(self.label_attack, 2, 0)
        layout_gird_monster.addWidget(self.monster_attack, 2, 1)
        layout_gird_monster.addWidget(self.label_defense, 3, 0)
        layout_gird_monster.addWidget(self.monster_defense, 3, 1)

        self.combat_view = QtGui.QTextBrowser()

        self.playerPropertyLayout.addLayout(layout_gird_player)
        self.monsterPropertyLayout.addLayout(layout_gird_monster)
        self.mainLayout.addLayout(self.playerPropertyLayout)
        self.mainLayout.addLayout(self.monsterPropertyLayout)
        self.mainLayout.addLayout(self.combatViewLayout)

        self._init_player()
        self._init_monter()

    def _init_player(self):
        player = Player()
        self.player_name.setText(player.name)
        self.player_level.setText(str(player.level))
        self.player_strength.setText(str(player.strength))
        self.player_endurance.setText(str(player.endurance))
        self.player_dexterity.setText(str(player.dexterity))
        self.player_intellect.setText(str(player.intellect))
        self.player_life.setText(str(player.life))
        self.player_attack.setText(str(player.attack))
        self.player_defense.setText(str(player.defense))

    def _init_monter(self):
        monster = Monster()
        self.monster_name.setText(str(monster.name))
        self.monster_life.setText(str(monster.life))
        self.monster_attack.setText(str(monster.attack))
        self.monster_defense.setText(str(monster.defense))

    def combat(self):
        monster_life = int(self.monster_life.text())
        monster_attack = int(self.monster_attack.text())
        monster_defense = int(self.monster_defense.text())
        player_life = int(self.player_life.text())
        player_attack = int(self.player_attack.text())
        player_defense = int(self.player_defense.text())
        while monster_life > 0 and player_life > 0:
            monster_life = monster_life - player_attack + monster_defense
            if monster_attack > player_defense:
                player_life = player_life - monster_attack + player_defense
            self.player_life.setText(str(player_life))
            self.monster_life.setText(str(monster_life))
            time.sleep(0.3)


class Player(Base_Mode.Person):
    def __init__(self):
        super(Player, self).__init__()


class Monster(Base_Mode.Monster):
    def __init__(self):
        super(Monster, self).__init__()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    model = Model()
    controller = Controller(model)
    MainApp = MainUI(model, controller)
    MainApp.show()
    tr = threading.Thread(target=MainApp.combat)
    tr.start()
    sys.exit(app.exec_())
