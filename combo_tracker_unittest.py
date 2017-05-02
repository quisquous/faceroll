from dps import ComboTracker
import unittest

class ComboTrackerBasic(unittest.TestCase):
    def runTest(self):
        c = ComboTracker([range(1, 10)], [])
        self.assertEqual(c.current_node, None)
        for i in range(1, 10):
            self.assertTrue(c.would_continue_combo(i))
            self.assertTrue(c.apply_skill(i))
            self.assertEqual(c.current_node, i)


class ComboTrackerBasicRestart(unittest.TestCase):
    def runTest(self):
        c = ComboTracker([range(1, 5), [5, 6], [7]], [])
        starters = [1, 5, 7]

        # verify that the chain can transition to a starter at any step in
        # in at least the basic 1..5 chain
        for s in starters:
            for i in range(1, 5):
                for j in range(1, i + 1):
                    self.assertTrue(c.apply_skill(j))
                self.assertEqual(c.current_node, i)
                self.assertTrue(c.apply_skill(s))
                self.assertEqual(c.current_node, s)


class ComboTrackerIgnores(unittest.TestCase):
    def runTest(self):
        ignores = ['x', 'y', 'z']
        c = ComboTracker([range(1, 10)], ignores)

        self.assertEqual(c.current_node, None)
        self.assertFalse(c.apply_skill(ignores[0]))
        self.assertEqual(c.current_node, None)

        # verify all the ignores work at every step in the chain
        for i in range(1, 10):
            self.assertTrue(c.apply_skill(i))
            for ignore in ignores:
                self.assertFalse(c.apply_skill(ignore))
                self.assertEqual(c.current_node, i)


class ComboTrackerBreak(unittest.TestCase):
    def runTest(self):
        c = ComboTracker([range(1, 5)], [])

        breakers = ['x', 'y', 'z', 11, 12]

        self.assertEqual(c.current_node, None)
        self.assertFalse(c.apply_skill(breakers[0]))
        self.assertEqual(c.current_node, None)

        for i in range(1, 5):
            for j in range(1, i + 1):
                c.apply_skill(j)
            self.assertEqual(c.current_node, i)
            self.assertFalse(c.apply_skill(breakers[i]))
            self.assertEqual(c.current_node, None)


class ComboTrackerMulti(unittest.TestCase):
    def runTest(self):
        chains = [
            [1, 2, 3],
            [1, 5, 6],
            [4, 7, 8],
            [1, 5, 9]
        ]
        c = ComboTracker(chains, [])

        starters = [1, 4]



if __name__ == '__main__':
    unittest.main()
