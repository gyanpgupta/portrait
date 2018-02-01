import base64

from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UploadImageForm


def upload_image(request):
    form = UploadImageForm()
    return render(request, 'content_upload/upload_image.html', {'form': form })


def result_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            myimage = base64.b64encode(image.file.read())
            return render(request, 
                'content_upload/result_image.html',
                {'image_src': myimage}
            )
        return render(request, 'content_upload/upload_image.html', {'form': form})
    return HttpResponseRedirect(reverse('upload_image'))