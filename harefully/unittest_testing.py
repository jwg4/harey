import unittest

def test_case(c):
    if issubclass(unittest.TestCase, c):
        return unittest.TestCase
    c = type(
        '%s_extended_with_unittest__TestCase' % (c.__name__, ), 
        (c, unittest.TestCase), 
        {}
    )
    def test_fn(s):
        return None
    for test in c.tests:
        setattr(c, 'test_asdf', test_fn)
    return c
