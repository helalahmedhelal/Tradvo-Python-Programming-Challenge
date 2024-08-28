
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadedAppForm
from .models import UploadedApk
from .tasks import run_appium_task


    
# Create your views here.
def interface(request):
    return render(request,'interface/interface.html')

@login_required
def apk_list(request):
    apks = UploadedApk.objects.filter(uploaded_by=request.user)
    context={'apks': apks}
    return render(request, 'interface/uploadedapks/apk_list.html',context)

@login_required
def apk_add(request):
    if request.method == 'POST':
        form = UploadedAppForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.uploaded_by = request.user
            app.save()
            return redirect('apk_list')
    else:
        form = UploadedAppForm()
    
    context={'form': form}    
    return render(request, 'interface/uploadedapks/apk_add.html', context )


@login_required
def apk_details(request,pk):
    app_data = get_object_or_404(UploadedApk, pk=pk, uploaded_by=request.user)
    context={'app_data': app_data}
    return render(request, 'interface/uploadedapks/apk_details.html',context)


@login_required    
def apk_update(request,pk):
    
    app = get_object_or_404(UploadedApk, pk=pk, uploaded_by=request.user)
    
    if request.method == 'POST':
        
       form=UploadedAppForm(request.POST,request.FILES,instance=app)
       
       if form.is_valid():
           
          form.save()
          
          return redirect('apk_details', pk=pk)
    else:  
        
       form=UploadedAppForm(instance=app)
    
    context={'form':form}
    
    return render(request,'interface/uploadedapks/apk_update.html',context)
  
   
@login_required
def apk_delete(request, pk):
    app_data = get_object_or_404(UploadedApk, pk=pk, uploaded_by=request.user)
    if request.method == 'POST':
        app_data.delete()
        return redirect('apk_list')
    context={'app_data': app_data}
    return render(request, 'interface/uploadedapks/apk_delete.html', context)    

@login_required
def run_appium(request, pk):
    app = get_object_or_404(UploadedApk, pk=pk, uploaded_by=request.user)
    
    if request.method == 'GET':
        # Trigger the Celery task
        run_appium_task.delay(request,app.pk)
        return redirect('apk_details')
    
    return render(request, 'interface/uploadedapks/waiting_appium_test_finish.html')