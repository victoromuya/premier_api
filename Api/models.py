from django.db import models

class SignupCourses(models.Model):
    
    def __str__(self):
        return self.course
    
    name = models.CharField(default="yourname", max_length=30)
    email = models.EmailField(default="email@yahoo.com")
    course = models.CharField(default="course", max_length=30)  
    
    class Meta:
        unique_together = ["email", "course"]
        
