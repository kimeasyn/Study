from django.shortcuts import render
from .models import Study
# Create your views here.


def study_list(request):
    qs = Study.objects.all()

    q = request.GET.get('q',' ')
    if q:
        qs = Study.objects.filter(title__icontains=q)
    return render(request, 'studyApp/study_list.html', {
        'study_list': qs,
        'q': q,
    })
