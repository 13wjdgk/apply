from django.shortcuts import render,get_object_or_404,redirect
from .models import Apply
from django.utils import timezone
# Create your views here.
def main(request):
    apply = Apply.objects
    return render(request,'main.html',{'apply':apply})

def create(request):
    return render(request,'create.html')

def detail(request,apply_id):
    apply_detail = get_object_or_404(Apply,pk=apply_id)
    return render(request,'detail.html',{'apply_detail':apply_detail})

def create_apply(request):
    apply = Apply()
    apply.name = request.GET['name']
    apply.text = request.GET['text']
    apply.age = request.GET['age']
    apply.pub_date = timezone.datetime.now()
    if 'woman' in request.GET['gender']:
        apply.gender=True
    else: apply.gender=False
    apply.save()
    return redirect('/detail/'+str(apply.id))