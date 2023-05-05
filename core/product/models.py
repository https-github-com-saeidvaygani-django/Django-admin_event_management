from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator

class Students(models.Model):
    National_id = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    Student_id = models.CharField(max_length=8, unique=True, validators=[MinLengthValidator(8),MaxLengthValidator(8)])
    First_name = models.CharField(null=False, unique=False, max_length=50, blank=False)
    Last_name = models.CharField(null=False, unique=False, max_length=50, blank=False)
    Birth_date = models.DateField()
    City_born = models.CharField(max_length=50)
    Date_enterance = models.DateField()
    major = models.ManyToManyField('Major', verbose_name='Majors')
    study_courses = models.ManyToManyField('Courses')
    Units_numbers = models.CharField(max_length=3)
    is_study_now = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, editable=True)
    image = models.ImageField(upload_to='media/Students/', validators=[FileExtensionValidator(['jpg', 'png'])])
    
    def Calculate_Units_numbers(self):
        total_units = 0
        
        for study_courses in self.study_courses.all():
            total_units += study_courses.Course_credit
        
        self.Units_numbers = total_units 
        self.save()

    def __str__(self):
        return self.First_name + self.Last_name

class Instructors(models.Model):
    National_id = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    Instructor_id = models.CharField(max_length=9, unique=True, validators=[MinLengthValidator(9),MaxLengthValidator(9)])
    First_name = models.CharField(null=False, unique=False, max_length=50, blank=False)
    Last_name = models.CharField(null=False, unique=False, max_length=50, blank=False)
    Birth_date = models.DateField(auto_now_add=True, editable=True)
    City_born = models.CharField(max_length=50)
    Instructor_degree = models.ForeignKey('Major', on_delete=models.CASCADE)
    Teach_courses_id = models.ManyToManyField('Courses')
    Instructor_salary = models.IntegerField()
    is_instructor_now = models.BooleanField(default=True)
    Description_Instructor = models.TextField(max_length=200)
    image = models.ImageField(upload_to='media/Instructors/', validators=[FileExtensionValidator(['jpg', 'png'])])
    
    def __str__(self):
        return self.First_name + self.Last_name

class Major(models.Model):
    majors = models.CharField(max_length=50)
    
    def __str__(self):
        return self.majors
    

class Courses(models.Model):
    Name_course = models.CharField(max_length = 50 )
    Course_credit = models.IntegerField()
    Major_id = models.ForeignKey(Major, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.Name_course
    
    