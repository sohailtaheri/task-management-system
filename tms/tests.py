from django.test import TestCase
from django.utils.timezone import now, timedelta
import random
import unittest
from tms.models import ProjectModel, TaskModel

class ProjectAndTaskTestCase(TestCase):
    def setUp(self):
        # Create ProjectModel instances
        self.project1 = ProjectModel.objects.create(title="Project Alpha", description="Description for Project Alpha")
        self.project2 = ProjectModel.objects.create(title="Project Beta", description="Description for Project Beta")
        self.project3 = ProjectModel.objects.create(title="Project Gamma", description="Description for Project Gamma")

        # Create TaskModel instances and assign them randomly to projects
        self.projects = [self.project1, self.project2, self.project3]
        self.tasks = []
        for i in range(7):
            task = TaskModel.objects.create(
                title=f"Task {i+1}",
                description=f"Description for Task {i+1}",
                project=random.choice(self.projects),
                priority=random.choice(['low', 'medium', 'high']),
                due_date=now().date() + timedelta(days=random.randint(1, 30))
            )
            self.tasks.append(task)

    def test_project_creation(self):
        self.assertEqual(ProjectModel.objects.count(), 3)
        self.assertTrue(ProjectModel.objects.filter(title="Project Alpha").exists())
        self.assertTrue(ProjectModel.objects.filter(title="Project Beta").exists())
        self.assertTrue(ProjectModel.objects.filter(title="Project Gamma").exists())

    def test_task_creation(self):
        self.assertEqual(TaskModel.objects.count(), 7)
        for i in range(7):
            self.assertTrue(TaskModel.objects.filter(title=f"Task {i+1}").exists())

    def test_task_project_assignment(self):
        for task in self.tasks:
            self.assertIn(task.project, self.projects)

    def test_task_priority(self):
        valid_priorities = ['low', 'medium', 'high']
        for task in self.tasks:
            self.assertIn(task.priority, valid_priorities)

    def test_task_due_date(self):
        for task in self.tasks:
            self.assertGreaterEqual(task.due_date, now().date())

if __name__ == "__main__":
    unittest.main()