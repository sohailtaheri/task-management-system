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
        users = User.objects.all()
        if not users.exists():  # if no users exist, create 3 users
            user = User.objects.create_superuser(username='admin', password='842390@aut', superuser=True)
            for i in range(2):
                user = User.objects.create_user(
                    username=f'user{i+1}',
                    password='842390@aut',
                )

        # create projects
        projects = []
        for user in users:
            project = ProjectModel.objects.create(
                title       = f"Project {user.id}",
                description = lorem_ipsum.paragraph(),
                owner       = user
            )
            projects.append(project)
            print(f"Created project: {project.title}")
        
        # create tasks
        for i in range(10):
            task = TaskModel.objects.create(
                title       = f"Task {i+1}",
                description = lorem_ipsum.paragraph(),
                project     = random.choice(projects),
                priority    = random.choice(['low', 'medium', 'high']),
                due_date    = now().date() + timedelta(days=random.randint(1, 30)),
                status      = random.choice(['pending', 'in_progress', 'completed']),
                created_by  = random.choice(users),
                assigned_to = random.choice(users),
            )
            print(f"Created task: {task.title} for project: {task.project.title}")