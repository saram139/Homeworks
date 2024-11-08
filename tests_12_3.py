import runner
import runner_and_tournament as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner_1 = runner.Runner("Max")
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner_2 = runner.Runner("Alex")
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_3 = runner.Runner("Den")
        runner_4 = runner.Runner("Anton")
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = rt.Runner("Усэйн", 10)
        self.runner_2 = rt.Runner("Андрей", 9)
        self.runner_3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        tournament_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        finishers = {i: str(j) for i, j in tournament_1.start().items()}
        self.all_results.append(finishers)
        self.assertTrue(max(finishers.keys()), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        tournament_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        finishers = {i: str(j) for i, j in tournament_2.start().items()}
        self.all_results.append(finishers)
        self.assertTrue(max(finishers.keys()), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        tournament_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        finishers = {i: str(j) for i, j in tournament_3.start().items()}
        self.all_results.append(finishers)
        self.assertTrue(max(finishers.keys()), "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_4(self):
        tournament_4 = rt.Tournament(3, self.runner_1, self.runner_2, self.runner_3)
        finishers = tournament_4.start()
        self.assertEqual(finishers[1], "Усэйн")
        self.assertEqual(finishers[2], "Андрей")
        self.assertEqual(finishers[3], "Ник")


if __name__ == "__main__":
    unittest.main()
