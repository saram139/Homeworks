import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runner.Runner("Max")
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner("Alex")
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = runner.Runner("Den")
        runner_4 = runner.Runner("Anton")
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == "__main__":
    unittest.main()
