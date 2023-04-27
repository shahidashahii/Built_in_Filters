from django.shortcuts import render

# Create your views here.
def  built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'SHaHIda is A BEautifUL Girl','dt':dt,'c':9}
    return render(request,'built_in_filters.html',d)