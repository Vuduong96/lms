from django.db import models

# Instructor Model
class Instructor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        verbose_name_plural="1. Instructor"



# Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    # Create class Meta for modification
    class Meta:
        verbose_name_plural="2. Course Categories"


# Course Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory,
                        on_delete=models.CASCADE)
    instructor=models.ForeignKey(Instructor, 
                        on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()

    class Meta:
        verbose_name_plural="3. Courses"

# Student  Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    interested_catgories=models.TextField()

    class Meta:
        verbose_name_plural="4. Students"