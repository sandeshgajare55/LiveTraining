try:
    A = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
    A['Michael']
except KeyError:
    print('KeyError')