from django.template.response import TemplateResponse
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from student.models import Student, StudentMarksMetaInfo, Marks

def index(request):
    return TemplateResponse(request, 'index.html', {})


@csrf_exempt
def usn_search(request):
    try:
        student_obj = Student.objects.get(usn=request.POST.get('usn').upper())
    except:
        return HttpResponse("sorry no results found")
    else:

        context_dict = {"student": student_obj,
                        "student_marks_meta_info": StudentMarksMetaInfo.objects.filter(student=student_obj)}
        return render(request, 'marks_meta_page.html', context_dict)


@csrf_exempt
def marks_details(request, id):
    marks_object_list = Marks.objects.filter(student_marks_meta_info__id=id)

    if not marks_object_list:
        return HttpResponse("Are you Lost ?")

    return render(request, 'marks_details.html', {'marks_list': marks_object_list})
