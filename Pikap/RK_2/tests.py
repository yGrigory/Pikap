import unittest
from RK2.RK1_refactored import (
    orchestras, works, works_orchestras,
    get_one_to_many, get_many_to_many,
    query_d1, query_d2, query_d3
)


class TestMusicQueries(unittest.TestCase):

    def setUp(self):
        self.one_to_many = get_one_to_many(orchestras, works)
        self.many_to_many = get_many_to_many(orchestras, works, works_orchestras)

    def test_query_d1_titles_ending_with_ov(self):
        result = query_d1(self.one_to_many)

        expected = {
            ("Вальсов", "Академический оркестр"),
            ("Маршов", "Симфонический оркестр"),
            ("Концертов", "Академический оркестр"),
        }

        self.assertEqual(set(result), expected)

    def test_query_d2_average_duration(self):
        result = query_d2(self.one_to_many, orchestras)

        orch_dict = dict(result)

        self.assertAlmostEqual(orch_dict["Камерный ансамбль"], 12.0)
        self.assertAlmostEqual(orch_dict["Симфонический оркестр"], 6.5)
        self.assertAlmostEqual(orch_dict["Академический оркестр"], 8.75)

    def test_query_d3_orchestras_starting_with_a(self):
        result = query_d3(self.many_to_many, orchestras)

        self.assertIn("Академический оркестр", result)
        self.assertIn("Альтернативный оркестр", result)
        self.assertIn("Вальсов", result["Академический оркестр"])


if __name__ == "__main__":
    unittest.main()
