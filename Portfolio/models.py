from django.db import models

# Create your models here.
class About_me(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"