'''
Author: ShadowLcz
Date: 2025-01-29 07:09:28
LastEditTime: 2025-06-04 22:43:45
LastEditors: ShadowLcz
Description: 
FilePath: /lab/lab01/tests/q2d.py
'''
OK_FORMAT = True

test = {   'name': 'q2d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> valid_values\n'
                                               'array([0.95071431, 0.86617615, 0.96990985, 0.94888554, 0.96563203,\n'
                                               '       0.9093204 , 0.96958463, 0.93949894, 0.89482735, 0.92187424])',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> len(valid_values) == 10\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.allclose(valid_values, [0.95071431, 0.86617615, 0.96990985, 0.94888554, 0.96563203,\n'
                                               '...        0.9093204 , 0.96958463, 0.93949894, 0.89482735, 0.92187424])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
