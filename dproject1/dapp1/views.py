from django.shortcuts import render
from django.http import HttpResponse 
import datetime
from dapp1.models import student_details
from dapp1.models import author,books


# Create your views here.
# def land(request):
#     return render(request,"land.html")
# di={
#     "id":[1,2,3,4,5],
#     "name":["Pavan","nav","mang","bhar","phar"],
#     "loc":["hyd","ban","tpt","mango","grap"]
# }
# def details(request):
#     return render(request,"land.html",di)
# name=input("enter name:")
# def pname(request):
#     return render(request,"land.html",{"name":name})
# di = {
#     "id": [1, 2, 3, 4, 5],
#     "name": ["Pavan", "nav", "mang", "bhar", "phar"],
#     "loc": ["hyd", "ban", "tpt", "mango", "grap"]
# }
# def details(request):
#     data = zip(di["id"], di["name"], di["loc"])  # combine lists
#     return render(request, "land.html", {"data": data})
# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return render(request,"about.html")

#  creating database dynamically 

# def data_base(request):
#     course = []
#     n = int(input("enter the number of courses :"))
#     for i in range(n):
#         course_id = input("Enter id:")
#         course_name = input("Enter course name:")
#         duration = input("Enter the duration:")

#         course.append({
#             "course_id": course_id,
#             "course_name": course_name,
#             "duration": duration
#         })

#     print("\nCollected Data:")
#     for c in course:
#         print(c["course_id"], c["course_name"], c["duration"])

#     return render(request, 'land.html', {'course': course})

# l=[]
# n=int(input("Enter no of elements in list:"))
# for i in range(n):
#     b=int(input("Enter element in list:"))
#     l.append(b)

# def list_data(request):
#     return render(request,'land.html',{'l':l})


# def c_datetime(request):
#     time_now = datetime.datetime.now()  
#     html = f"<h1>Current Date and Time:</h1> <p>{time_now}</p>"
#     return HttpResponse(html)

# name=input("Enter name")
# age=int(input("enter age:"))
# location=input("Enter loc:")

# def details(request):
#     return render(request, 'land.html', {
#     'name': name,
#     'age': age,
#     'location': location
# })

# def emp_details(request):
#     l=[]
#     n=int(input("Enter no.of elelments in list"))
#     for i in range(n):
#         id=int(input("Enter id"))
#         name=input("Enter name:")
#         role=input("enter role:")
#         l.append({
#             'id':id,
#             'name':name,
#             'role':role
#         })
#     for j in l:
#         print(j['id'],j['name'],j['role'])
    
#     return render(request,'land.html',{'l':l})

# dic={
#     'name':'pavan',
#     'age':20,
#     'location':'bangalore'
# }
# def dictionary(request):
#     return render(request,'land.html',{'dic':dic})

# def b(request):
#     a=student_details.objects.all()
#     return render(request,"land.html",{'student_details':a})

def book_list(request):
    book_data=books.objects.all()
    return render(request,'land.html',{'books':book_data})









