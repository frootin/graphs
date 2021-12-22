import unittest
from graphs_type import is_full_connected, connection_type, main


class TestIsFull(unittest.TestCase):
    def test_strange_input(self):
        res = is_full_connected(0, 1)
        self.assertFalse(res)

    def test_full(self):
        res = is_full_connected(4, 6)
        self.assertTrue(res)

    def test_not_full(self):
        res = is_full_connected(4, 3)
        self.assertFalse(res)


class TestNotFullConnections(unittest.TestCase):
    def test_uncertain(self):
        res = connection_type(3, 2, [(1, 2), (2, 1), (2, 3), (3, 2)])
        self.assertEqual(res, 4)

    def test_mixed_type(self):
        res = connection_type(5, 5, [(1, 2), (2, 1), (1, 3), (3, 1), (1, 4),
                                     (4, 1), (1, 5), (5, 1), (2, 3),(3, 2)])
        self.assertEqual(res, 4)

    def test_ring(self):
        res = connection_type(5, 5, [(1, 2), (2, 1), (2, 3), (3, 2), (3, 4),
                                     (4, 3), (4, 5), (5, 4), (5, 1), (1, 5)])
        self.assertEqual(res, 1)

    def test_bus(self):
        res = connection_type(5, 4, [(1, 2), (2, 1), (2, 3), (3, 2),
                                     (3, 4), (4, 3), (4, 5), (5, 4)])
        self.assertEqual(res, 2)

    def test_star(self):
        res = connection_type(5, 4, [(1, 2), (2, 1), (1, 3), (3, 1),
                                     (1, 4), (4, 1), (1, 5), (5, 1)])
        self.assertEqual(res, 3)


class TestAsProgram(unittest.TestCase):
    def test_main(self):
        with self.assertRaises(SystemExit) as e:
            main(["5", "4", "1", "2", "2", "1", "1", "3",
                  "3", "1", "1", "4", "4", "1", "1", "5", "5", "1"])
        exc = e.exception
        self.assertEqual(exc.code, 0)

    def test_main_full(self):
        with self.assertRaises(SystemExit) as e:
            main(["3", "3", "1", "2", "2", "1", 
                  "1", "3", "3", "1", "2", "3", "3", "2"])
        exc = e.exception
        self.assertEqual(exc.code, 0)
