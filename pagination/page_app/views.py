from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .forms import *
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

# Create your views here.
def index(request):
    if request.method=='POST':
        form=info_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
           
    else:
        form=info_form()
    
    return render(request, 'index.html', {'form':form})

def display(request):
    show= Info.objects.all()
    p=Paginator(show,4)
    page_number=request.GET.get('page')
    try:
        page_obj= p.get_page(page_number)
        
    except EmptyPage:
        page_obj=p.page(p.num_pages)
    context= {'page_obj':page_obj}   
    return render(request, 'display.html', context)





def delete(request, id):
    d= Info.objects.get(id=id)
    d.delete()
    return redirect('display')




def update(request, id):
    instance = get_object_or_404(Info, id=id)
    if request.method == 'POST':
        form = info_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('display')  # Redirect to a display page or another view
    else:
        form = info_form(instance=instance)

    return render(request, 'update.html', {'form': form})