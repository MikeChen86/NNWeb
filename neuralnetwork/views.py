from django.shortcuts import render, redirect
from .forms import UploadImageForm
from django.contrib import messages
from django.views import generic
from .models import UploadImage
# Create your views here.


def homepage(request):
    return render(request, 'neuralnetwork/homepage.html')


def image_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '上傳成功')
            return redirect(request, 'image_detail')
        else:
            messages.error(request, '上傳失敗')
    else:
        form = UploadImageForm()
    return render(request, 'neuralnetwork/image_upload.html', {'form': form})


class ShowImage(generic.DetailView):
    model = UploadImage
    template_name = 'neuralnetwork/image_detail.html'


class ImageList(generic.ListView):
    model = UploadImage
    template_name = 'neuralnetwork/image_list.html'
