from random import randint
from characters import *


def takeDmg(attacker, defender):
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['hp'] = defender['stats'][hp] - dmg
    if defender['stats']['hp'] <= 0:
        print('{] has been defeated'/format(defender['name']))
        char['xp'] += dragon['xp_gain']
        return
    else:
        print('{} has taken {} points of damage.'.format(defender{'name'}, dmg))


def commands(player, opponent):
    while True:
        print('------------------')
        cmd = input('would you like to attack? (y/n)').lower()
        if 'y' in cmd:
            print('{} summons courage into a brazen attack.'.format(player['name']))
            takeDmg(player, opponent)
        elif 'no' in cmd:
            print('{} doesnt hesitate to attack'.format(enemy['name']))
            takeDmg(player, opponent)
        else:
            pass