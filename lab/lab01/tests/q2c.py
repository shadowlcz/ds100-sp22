'''
Author: ShadowLcz
Date: 2025-01-29 07:09:28
LastEditTime: 2025-06-04 22:43:36
LastEditors: ShadowLcz
Description: 
FilePath: /lab/lab01/tests/q2c.py
'''
OK_FORMAT = True

test = {   'name': 'q2c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> population_0 = np.random.randn(100)\n>>> np.isclose(mean(population_0), np.mean(population_0), atol=1e-6)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> population_0 = np.random.randn(100)\n>>> np.isclose(variance(population_0), np.var(population_0), atol=1e-6)\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
