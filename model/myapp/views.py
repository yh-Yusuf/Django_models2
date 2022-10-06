from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def del_record(request, x):
    z = Post.objects.get(id=x)
    z.delete()
    return HttpResponseRedirect("/")



def index(request):
    # stu_object = Student_info(name = 'Johnn', address = 'kdghd', marks = 67)
    # stu_object.save()

    # Fetch and Update
    q = Post.objects.get(id=3)
    q.title = 'new address'
    q.save()

    # Deleting record
    # q = Post.objects.get(id=3)
    # q.delete()


    records = Post.objects.all()
    print(records)

    context_dic = {'info': records}
    return render(request, 'index.html', context_dic)