from django.db import models


class ProjectModel(models.Model):

    title       = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    created_by  = models.ForeignKey('auth.User', 
                                    on_delete=models.CASCADE, 
                                    related_name='projects', 
                                    default=1)  # Assuming the user with ID 1 exists as the default user

    def __str__(self): 
        return f"{self.title} crated by {self.created_by.username}"



class TaskModel(models.Model):
    
    STATUS_CHOICES = [
        ('pending'    , 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed'  , 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low'   , 'Low'),
        ('medium', 'Medium'),
        ('high'  , 'High'),
    ]

    title       = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)
    project     = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority    = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date    = models.DateField(blank=True, null=True)
    created_by  = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE, 
        related_name='tasks', 
        default=1  # Assuming the user with ID 1 exists as the default user
    )

    def __str__(self):
        return self.title

