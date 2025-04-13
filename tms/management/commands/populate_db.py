import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import User
from tms.models import ProjectModel, TaskModel

class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create super user
        user = User.objects.filter(username='admin').first()
        if not user: 
            user = User.objects.create_superuser(username='admin', password='842390')

        # create projects
        projects = []
        for i in range(3):
            project = ProjectModel.objects.create(
                title=f"Project {i+1}",
                description=lorem_ipsum.paragraph(),
                created_by=user
            )
            projects.append(project)
            print(f"Created project: {project.title}")
        # create tasks
        for i in range(10):
            task = TaskModel.objects.create(
                title=f"Task {i+1}",
                description=lorem_ipsum.paragraph(),
                project=random.choice(projects),
                priority=random.choice(['low', 'medium', 'high']),
                due_date=now().date() + timedelta(days=random.randint(1, 30))
            )
            print(f"Created task: {task.title} for project: {task.project.title}")