import module_12_1
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = module_12_1.Runner('Cat')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = module_12_1.Runner('Dog')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = module_12_1.Runner('Dog')
        runner_2 = module_12_1.Runner('Cat')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == 'main':
    unittest.main()
