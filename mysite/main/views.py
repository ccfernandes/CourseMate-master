from django.shortcuts import render #render is for templates
from django.http import HttpResponse 
from .models import Tutorial, School, Course, SchoolCourse
from main.forms import CourseForm, SchoolCourseForm, SchoolForm
 
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import datetime


# Create your views here.
def homepage(request): #for any view, always pass request 
    school_list = School.objects.order_by('name')
    
    return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/home.html", context = {'school_list' : school_list})

def review(request):
	my_form=CourseForm()
	# course_form=SchoolCourseForm()
	course_list = SchoolCourse.objects.all()
	if request.method == "POST":
		my_form = CourseForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			# Course.objects.create(my_form.cleaned_data)
			my_form.save()
			return render(request=request, template_name="main/course.html", context={'my_form': my_form, 'course_list': course_list})
		else:
			print(my_form.errors)
					#once u make a review, it should direct u to the class page 
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/review.html", context={"form": my_form,'course_list': course_list})

def SearchPage(request):
 	query=request.GET.get('q', '')
 	if query:
 		result=School.objects.filter(name__icontains=query)
 	else:
 		result=[]	
 	# queryset=School.objects.order_by('name')
 	return render(request=request, template_name="main/search.html", context={"result": result})

# class SearchPage(ListView):
# 	model=School
# 	template_name='main/search.html'
# 	# queryset=School.objects.filter(name__icontains="Santa Clara University")
# 	def get_queryset(self):
# 	# 	return School.objects.filter(name__icontains="Santa Clara University")
# 		return School.objects.filter(Q(name__icontains='Boston') | Q(abbrev__icontains='UCSB'))

def course(request, course_id, my_id):
	def get(self, request):
		form=CourseForm()
		posts=Course.objects.get(id=my_id).order_by('name')
		print(posts)
		return render(request=request, template_name="main/course.html", context={'posts': posts})
	posts=Course.objects.order_by("name")
	return render(request=request, template_name="main/course.html", context={'posts': posts})

def college(request, my_id):
	query=request.GET.get('q', '')
	if query:
		result=School.objects.filter(name__icontains=query)
	else:
		result=[]
	# def get(self, request):
	form=SchoolCourseForm()
	posts=SchoolCourse.objects.exclude(name__isnull=True)
	print(posts)
	return render(request=request, template_name="main/uniBase.html", context={'posts': posts, 'result': result})

def addCourse(request, my_id):
	print("hello")
	my_form =SchoolCourseForm()
	if request.method=="POST":
	# print("post")
		my_form = SchoolCourseForm(request.POST)
		if my_form.is_valid():
			my_form.save()
			# my_form.cleaned_data
			print("saved)")
			return render(request=request, #so u can reference things inside your template to do with the user
	                  template_name="main/.html", context={"form": my_form})
		else:
			my_form=SchoolCourseForm()
			print("error")
			print(my_form.errors)
	print("done")
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/addCourse.html", context={"form": my_form})

def about(request):
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/AboutUs.html")
def login(request):
	now=datetime.datetime.now()
	return render(request=request, template_name="main/login.html", context={'datetime_now':now})

def current_date_time(request):
	now=datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)


 
