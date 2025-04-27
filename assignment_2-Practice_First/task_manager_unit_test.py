# Group: Joseph Stefanoni, Hala Basyouni, Shrihit Saxena, Alice Zaytseva
# python -m unittest task_manager_unit_test.py
import unittest
from task_manager import add_task, remove_task, view_tasks, number_of_tasks, reset_list

class TestTodoListMethods(unittest.TestCase):
    def test_add_task(self):
        add_task("Buy groceries")
        self.assertIn("Buy groceries", view_tasks())
        reset_list()

    def test_remove_task(self):
        add_task("Do laundry")
        remove_task("Do laundry")
        self.assertNotIn("Do laundry", view_tasks())
        reset_list()

    def test_view_tasks(self):
        add_task("Walk the dog")
        self.assertEqual(view_tasks(), ["Walk the dog"])
        reset_list()

    def test_number_of_tasks(self):
        add_task("Wake up")
        add_task("Eat")
        add_task("Sleep")
        self.assertEqual(number_of_tasks(), 3)
        reset_list()

if __name__ == "__main__":
    unittest.main()
