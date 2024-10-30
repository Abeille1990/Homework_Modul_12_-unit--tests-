import runner_and_tournament as rt
from runner import Runner
import unittest
from wrapper_my import skip_if_frozen


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = rt.Runner('Усэйн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)

    # @classmethod
    # def tearDown(cls):
    #     print(cls.all_results)

    @skip_if_frozen
    def test_tournament1(self):
        tournament = rt.Tournament(90, self.r1, self.r3)
        result_1 = tournament.start()

        for i in range(len(result_1)):
            self.all_results[i + 1] = result_1[i + 1].name

        keys = list(self.all_results.keys())
        last = max(keys)
        last_name = self.all_results.get(last)

        self.assertTrue(last_name == 'Ник')

    @skip_if_frozen
    def test_tournament2(self):
        tournament = rt.Tournament(90, self.r2, self.r3)
        result_2 = tournament.start()

        for i in range(len(result_2)):
            self.all_results[i + 1] = result_2[i + 1].name

        res = self.all_results.get(max(self.all_results.keys()))

        self.assertTrue(res == 'Ник')

    @skip_if_frozen
    def test_tournament3(self):
        tournament = rt.Tournament(90, self.r2, self.r1, self.r3)
        result_3 = tournament.start()

        for i in range(len(result_3)):
            self.all_results[i+1] = result_3[i+1].name

        res = self.all_results.get(max(self.all_results.keys()))

        self.assertTrue(res == 'Ник')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        r1 = Runner('Alex')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    @skip_if_frozen
    def test_walk(self):
        w1 = Runner('Alex')
        for i in range(10):
            w1.walk()
        self.assertEqual(w1.distance, 50)

    @skip_if_frozen
    def test_challenge(self):
        r1 = Runner('Alex')
        w1 = Runner('Polly')

        for i in range(10):
            r1.run()

        for j in range(10):
            w1.walk()

        self.assertNotEqual(r1.distance, w1.distance)


if __name__ == '__main__':
    unittest.main()
