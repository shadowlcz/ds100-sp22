'''
Author: ShadowLcz
Date: 2025-01-29 07:09:28
LastEditTime: 2025-06-04 22:43:29
LastEditors: ShadowLcz
Description: 
FilePath: /lab/lab01/tests/q2b.py
'''
OK_FORMAT = True

test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> elementwise_array_sum([], [])\narray([], dtype=float64)', 'hidden': False, 'locked': False},
                                   {'code': '>>> elementwise_array_sum([1], [1])\narray([2])', 'hidden': False, 'locked': False},
                                   {'code': '>>> elementwise_array_sum([-1], [1])\narray([2])', 'hidden': False, 'locked': False},
                                   {'code': '>>> elementwise_array_sum([1], [-1])\narray([0])', 'hidden': False, 'locked': False},
                                   {'code': '>>> elementwise_array_sum([1, 2, 3], [1, 2, 3])\narray([ 2, 12, 36])', 'hidden': False, 'locked': False},
                                   {'code': '>>> elementwise_array_sum([1, 5, 2], [3, 6, 6])\narray([ 28, 241, 220])', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(elementwise_array_sum([], [])) is np.ndarray\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
