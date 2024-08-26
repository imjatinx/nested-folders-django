from django.shortcuts import render, redirect
from .models import Folder

# Create your views here.
def home(request):
    return render(request, 'index.html')


def create_folder(request, parent_id=None):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Folder.objects.create(name=name, parent_id=parent_id)
        return redirect('folder_list')
    return render(request, 'create_folder.html', {'parent_id': parent_id})


def folder_list(request, folder_id=None):
    if folder_id:
        folder = Folder.objects.get(id=folder_id)
        subfolders = folder.subfolders.all()
    else:
        subfolders = Folder.objects.filter(parent=None)
    return render(request, 'folder_list.html', {'subfolders': subfolders, 'parent_id': folder_id})

