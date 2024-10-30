import unittest
import tests_12_3 as t12_3

rtTS = unittest.TestSuite()
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(t12_3.TournamentTest))
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(t12_3.RunnerTest))

starter = unittest.TextTestRunner(verbosity=2)
starter.run(rtTS)

