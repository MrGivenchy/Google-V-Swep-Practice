import unittest
from task_scheduler import Task, dependency, completion_order


class TestTaskScheduler(unittest.TestCase):

    def test_part_2_dependencies(self):
        finance = Task(5, "Get finance approval", 2)
        parts = Task(3, "Get Parts", 1, [finance])
        technician = Task(4, "Get technician", 1)
        fix_bike = Task(2, "Fix bike", 0, [parts, technician])
        crossword = Task(1, "Solve the crossword", 3)
        lunch = Task(6, "Eat lunch", 0)

        tasks = [crossword, fix_bike, parts, technician, finance, lunch]
        result = dependency(tasks)

        self.assertIn(parts, result)
        self.assertIn(technician, result)
        self.assertIn(finance, result)
        self.assertNotIn(crossword, result)

    def test_part_3_completion_order(self):
        finance = Task(5, "Get finance approval", 2)
        parts = Task(3, "Get Parts", 1, [finance])
        technician = Task(4, "Get technician", 1)
        fix_bike = Task(2, "Fix bike", 0, [parts, technician])
        lunch = Task(6, "Eat lunch", 0)

        result = completion_order([fix_bike, parts, technician, finance, lunch])

        self.assertEqual(
            [task.description for task in result],
            [
                "Get finance approval",
                "Get Parts",
                "Get technician",
                "Fix bike",
                "Eat lunch"
            ]
        )

    def test_non_priority_zero_task_not_included(self):
        crossword = Task(1, "Solve crossword", 3)
        lunch = Task(2, "Eat lunch", 0)

        result = completion_order([crossword, lunch])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].description, "Eat lunch")


if __name__ == "__main__":
    unittest.main()