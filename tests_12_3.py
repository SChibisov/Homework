import unittest
import module_12_2 as test
import module_12_1


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в работе')
    def test_walk(self):
        runner = module_12_1.Runner('Cat')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в работе')
    def test_run(self):
        runner = module_12_1.Runner('Dog')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в работе')
    def test_challenge(self):
        runner_1 = module_12_1.Runner('Dog')
        runner_2 = module_12_1.Runner('Cat')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = test.Runner('Усэйн', 10)
        self.runer_2 = test.Runner('Андрей', 9)
        self.runer_3 = test.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament_1 = test.Tournament(90, self.runer_1, self.runer_3)
        result = tournament_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_tournament_1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        test_tournament_2 = test.Tournament(90, self.runer_2, self.runer_3)
        result = test_tournament_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_tournament_2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        test_tournament_3 = test.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = test_tournament_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_tournament_3'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_4(self):
        test_tournament_4 = test.Tournament(6, self.runer_1, self.runer_2, self.runer_3)
        result = test_tournament_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_tournament_4'] = result


if __name__ == '__main__':
    unittest.main()
