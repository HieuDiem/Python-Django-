from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import Http404, HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .forms import user_From, userForm
from .models import Person
# Create your views here.

# def index(request):
#     response = HttpResponse()
#     response.write("<h1>This is my first Django application</h1>")  
#     return response

# def detail(request, person_id):
#     return HttpResponse("You are looking at person %s ." % person_id)

# class IndexView(generic.ListView):
#     template_name = 'asigm_1_app/index.html'
#     content_object_name = 'person_list'
#     def get_queryset(self):
#         return Person.objects.all()

# class DetailView(generic.DetailView):
#     model = Person
#     template_name = 'asigm_1_app/detail.html'


def index(request):
    person_list = Person.objects.all()
    template = loader.get_template('asigm_1_app/index.html')
    context = {
        'person_list': person_list
    }
    return HttpResponse(template.render(context, request))
    

def detail(request, person_id):
    try:
        info_person = Person.objects.filter(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Question is not found")
    return render(request,  'asigm_1_app/detail.html', {'info_person': info_person})

# them person tu ke thua tu class Person()
def add(request):
    cont = {'uf':user_From}
    return render(request, 'asigm_1_app/add.html', cont )

def getAdd(request):
    if request.method == 'POST':
        uf = user_From(request.POST)
        if uf.is_valid():
            uf.save()
            return HttpResponse('save success')
    else:
        return HttpResponse('not POST')

#them person ko ke thua tu class Person()
def user(request):
    cont = {'uf': userForm()}
    return render(request, 'asigm_1_app/user.html', cont)

def useradd(request):
    if request.method == "POST":
        uf = userForm(request.POST)
        if uf.is_valid():
            # luu giu lieu tu ban goc (Model) cho Form
            saveUF = Person(id = uf.cleaned_data['id'],
                            name = uf.cleaned_data['name'],
                            age = uf.cleaned_data['age'],
                            address = uf.cleaned_data['address'],
                            mobile_number = uf.cleaned_data['mobile_number'])
            saveUF.save()
            return HttpResponse('success')
        else:
            return HttpResponse('form not value')
    else:
        return HttpResponse('not POST')