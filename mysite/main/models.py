from django.db import models
from datetime import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm

# Create your models here.

class Tutorial(models.Model): 
    tutorial_title=models.CharField(max_length=200)
    tutorial_content=models.TextField()
    tutorial_published=models.DateTimeField("data published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title



class School(models.Model):
    #fields 
    name=models.CharField(max_length=40)
    abbrev=models.CharField(max_length=15, null=False, default="")
    # location=models.CharField(max_length=30)

    def __str__(self):
    	return self.name

class SchoolForm(ModelForm):
	class Meta: 
		model = School
		fields = ['name']


# class Department(models.Model):
# 	name=models.CharField(max_length=30)
# 	school=models.ManyToManyField(School) #connects DepartmentName to School (i think)
# 	#many departments belong to one school 
	
# 	def __str__(self):
# 		return self.name

#the course itself
class SchoolCourse(models.Model):
	school=models.ForeignKey(School, blank=True, on_delete=models.DO_NOTHING, default="")

	courseNumber=models.CharField(max_length=10, blank=True, default="")
	name=models.CharField(max_length=100, blank=True, default="")

	def __str__(self):
		return self.courseNumber

class Meta:
		model = SchoolCourse
		fields = ['courseNumber', 'name']

#the reviews for each course 
class Course(models.Model):
	#general info
	courseNum=models.ForeignKey(SchoolCourse, blank=True, on_delete=models.DO_NOTHING, default="")

	courseNumber=models.CharField(max_length=10, blank=True, default="")
	name=models.CharField(max_length=100, blank=True, default="")
	
	professor_name=models.CharField(max_length=20, default="")
	
	#ratings, 1-10
	easyRating=models.CharField(
                                    # choices=[(,), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)
                                    choices=[('',''), ('1','1'), ('2','2'),('3','3'), ('4','4'), ('5','5')], blank=True, max_length=1, default="")
	InterestingRating=models.CharField(
    								choices=[('',''), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], blank=True, max_length=1, default="")

	numProjects=models.CharField(choices=[('',''), ('0','0'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), 
    									  	('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')], blank=True, max_length=2, default="")

	# department=models.ForeignKey(Department, on_delete=models.DO_NOTHING) #connects Course to DepartmentName
	#a class only belongs to a single department(usually)
	#the review itself, not data 

	numTests=models.CharField(
    							choices=[('',''), ('0','0'), ('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), 
    							('6', '6'), ('7', '7'),('8', '8'),('9', '9'), ('10', '10'), ('11', '11'), 
    							('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], blank=True, max_length=2, default="")
	testDiff=models.CharField(
    							choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True, max_length=1, default="")

	#amount of work
	time_spent=models.CharField(choices=[('',''), ('1', '0-2'), ('2', '3-4'), ('3', '5-6'), ('4', '7-8'), ('5', '9-10'), 
    							('6', '10-12'), ('7', '12-14'),('8', '15-17'),('9', '18-20'), ('10', '20+')],
    						 blank=True, max_length=5, default="")

	homework=models.CharField(choices=[('',''), ('True', 'Yes'), ('False', 'No')], blank=True, max_length=5, default="")
	pop_quizzes=models.CharField(choices=[('',''), ('True', 'Yes'), ('False', 'No')], blank=True, max_length=5, default="")
	webcast=models.CharField(choices=[('',''), ('True', 'Yes'), ('False', 'No')], blank=True, max_length=5, default="")

	gradeReceived=models.CharField(max_length=5, 
        choices=[('',''), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), 
                ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F', 'F'), 
                ('NP', 'NP'), ('P', 'P'), ('N/A', 'N/A')], blank=True, default="") 

	review_title=models.CharField("Review Title: ", max_length=100, blank=True, default="")
	review_content=models.CharField("Review Content: ", max_length=200, blank=True, default="")
	review_published=models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.review_title

# class CourseForm(ModelForm):
# 	class Meta: 
# 		model=Course 
# 		fields=[courseNumber, review_title, name, review_title, review_content, review_published
# 				professor_name, gradeReceived, easyRating, InterestingRating, homework
# 				pop_quizzes, webcast, numProjects, numTests, testDiff, time_spent]
				
