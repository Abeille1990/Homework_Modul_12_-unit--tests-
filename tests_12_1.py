from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_run(self):
        r1 = Runner('Alex')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_walk(self):
        w1 = Runner('Alex')
        for i in range(10):
            w1.walk()
        self.assertEqual(w1.distance, 50)

    def test_challenge(self):
        r1 = Runner('Alex')
        w1 = Runner('Polly')

        for i in range(10):
            r1.run()

        for j in range(10):
            w1.walk()

        self.assertNotEqual(r1.distance, w1.distance)


if __name__ == "__main__":
    unittest.main()