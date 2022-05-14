import os.path
import unittest

from repositories.history_repository import HistoryRepository


class TestHistoryRepository(unittest.TestCase):

    def setUp(self):
        self.history_repository = HistoryRepository()
        self.historyfile = "calculationhistory.txt"
        open(self.historyfile, "w").close()

    def test_file_exists(self):
        self.assertEqual(os.path.exists(self.historyfile), True)

    def test_file_not_exists(self):
        self.assertEqual(os.path.exists("thisfiledoesntexist.txt"), False)

    def test_adding_and_reading_historyfile(self):
        self.history_repository.add_calculation_to_history("1+", "1")
        self.history_repository.add_calculation_to_history("2+", "2")
        self.history_repository.add_calculation_to_history("3+", "3")
        self.assertEqual(
            len(self.history_repository.read_calculation_historyfile()), 3)

    def test_adding_unacceptable_inputs(self):
        self.history_repository.add_calculation_to_history("1/", "0")
        self.history_repository.add_calculation_to_history("2+", "2")
        self.history_repository.add_calculation_to_history("99**99", "3")
