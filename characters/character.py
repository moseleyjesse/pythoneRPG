
char = {
    'level': 1,
    'xp': 0,
    'level_up': 10
}
stats = {
    'hit points': 100,
    'power': 1,
}


def leveling(char, stats):
    n_hp, n_pwr = 0, 0
    while char['xp'] >= char['level_up']:
        char['level'] += 1
        char['xp'] = char['xp'] - char['level_up']
        char['level_up'] = round(char['level_up'] * 1.5)
        n_hp += 100
        n_pwr += 1

    print("level:", char['level'])
    print("Experience:", char['xp'])
    print("Next level required:", char['level_up'])
    print('hit points {} +{} \npower {} +{}'.format(stats['hit points'], n_hp,
                                                   stats['power'], n_pwr))

    stats['hit points'] += n_hp
    stats['power'] += n_pwr


char['xp'] += 10
leveling(char, stats)
print('--------------')

char['xp'] += 100
leveling(char, stats)
print('--------------')

char['xp'] += 1000
leveling(char, stats)
print('--------------')