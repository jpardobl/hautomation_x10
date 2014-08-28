import unittest
import cmds
import time


class TestX10(unittest.TestCase):

    def off_test_switch(self):
        self.assertRaises(ValueError, cmds.pl_switch("a1", "ooooo"))
        self.assertRaises(ValueError, cmds.pl_switch("af", "on"))
        self.assertRaises(ValueError, cmds.pl_switch("1f", "on"))
        self.assertRaises(ValueError, cmds.pl_switch("of", "on"))

    def off_test_switch_on(self):
        self.assertTrue(cmds.pl_switch("A5", "on"))
        time.sleep(5)

    def off_test_switch_off(self):
        self.assertTrue(cmds.pl_switch("A5", "off"))
        time.sleep(5)

    def test_all_lights_aff(self, ):
        print cmds.pl_all_lights_off("A")


  #TODO rest of the tests


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestX10)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unittest.main()
