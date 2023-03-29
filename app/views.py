from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]
job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description",
]

class TempClass:
    x = 5

def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name":"Django", "first_list":list, "temp_object": temp, "age":20, "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)

# Create your views here.
def job_list(request):
    # list_of_jobs = "<ul>"
    # for i in job_title:
    #     job_id = job_title.index(i)
    #     detail_url = reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs += f"<li><a href='job/{detail_url}'>{i}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    #return HttpResponse("<h1>Hello World</h1>")
    context = {"job_title_list":job_title}
    return render(request, "app/index.html", context)



def job_detail(request,id):
    # return HttpResponse(f"Job Detail Page {id}")
    #site = "https:/google.com"
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context = {"job_title":job_title[id], "job_description":job_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
    # "<domain>/job/1" --> Job detail page

