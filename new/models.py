from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    course_name = models.ForeignKey(Course, models.PROTECT)
    email = models.EmailField(unique=True)
    image = models.ImageField(blank=True,null=True, upload_to='images/')
    file = models.FileField(blank=True,null=True, upload_to='images/')
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

