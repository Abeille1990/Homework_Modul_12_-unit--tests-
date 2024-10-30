import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = rt.Runner('Усэйн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDown(cls):
        print(cls.all_results)

    def test_tournament1(self):
        tournament = rt.Tournament(90, self.r1, self.r3)
        result_1 = tournament.start()

        for i in range(len(result_1)):
            self.all_results[i + 1] = result_1[i + 1].name

        keys = list(self.all_results.keys())
        last = max(keys)
        last_name = self.all_results.get(last)

        self.assertTrue(last_name == 'Ник')

    def test_tournament2(self):
        tournament = rt.Tournament(90, self.r2, self.r3)
        result_2 = tournament.start()

        for i in range(len(result_2)):
            self.all_results[i + 1] = result_2[i + 1].name

        res = self.all_results.get(max(self.all_results.keys()))

        self.assertTrue(res == 'Ник')

    def test_tournament3(self):
        tournament = rt.Tournament(90, self.r2, self.r1, self.r3)
        result_3 = tournament.start()

        for i in range(len(result_3)):
            self.all_results[i+1] = result_3[i+1].name

        res = self.all_results.get(max(self.all_results.keys()))

        self.assertTrue(res == 'Ник')

if __name__ == '__main__':
    unittest.main()