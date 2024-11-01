import unittest
from rt_with_exceptions import Runner
import logging

logging.basicConfig(level=logging.INFO, filemode="w",
                    filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_run(self):
        try:
            r1 = Runner(True,5)
            for i in range(10):
                r1.run()
            self.assertEqual(r1.distance, 100)
            logging.info(f'"test_run" выполнен успешно', exc_info=True)
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_walk(self):
        try:
            w1 = Runner("Tanya", -5)
            for i in range(10):
                w1.walk()
            self.assertEqual(w1.distance, 50)
            logging.info(msg=f'"test_walk" выполнен успешно', exc_info=True)
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

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
