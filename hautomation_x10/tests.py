import unittest
import cmds


class TestX10(unittest.TestCase):

    def test_switch(self):
        self.assertRaises(ValueError, cmds.pl_switch("a1", "ooooo"))
        self.assertRaises(ValueError, cmds.pl_switch("af", "on"))
        self.assertRaises(ValueError, cmds.pl_switch("1f", "on"))
        self.assertRaises(ValueError, cmds.pl_switch("of", "on"))

    def test_switch_on(self):
        print "Hacmos los tests"
        self.assertTrue(cmds.pl_switch("A1", "on"))

    def test_switch_off(self):
        self.assertTrue(cmds.pl_switch("A1", "off"))
  #TODO rest of the tests


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
