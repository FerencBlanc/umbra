from django.db import models
class Level(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    depth_score = models.IntegerField()
    def __str__(self):
        return self.title
class Myth(models.Model):
    name = models.CharField(max_length=100)
    story = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return self.name