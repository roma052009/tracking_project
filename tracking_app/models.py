from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default=111)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stat = models.CharField(max_length=50)
    term = models.DateField()
    giver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_given", default=1)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_received", default=1)

class Comment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)