from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Study
from .forms import StudyForm
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


def study_detail(request, id):
    # try:
    #     study = Study.objects.get(id=id)
    # except Study.DoesNotExist:
    #     raise Http404

    study = get_object_or_404(Study, id=id)

    return render(request, 'studyApp/study_detail.html', {
        'study': study,
    })


def study_new(request):
    if request.method == 'POST':
        form = StudyForm(request.POST, request.FILES)
    else:
        form = StudyForm()

    return render(request, 'studyApp/study_form.html', {
        'form': form,
    })
