from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        #database=database.objects.filter(name__container=searched)
        return render(request,'core/search.html',{'searched':searched
                                                #,'database':database
                                                  })
    else:
        return render(request, 'core/search.html', {})