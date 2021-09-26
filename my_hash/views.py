from django.shortcuts import render
from .models import MyHash
from .forms import MyHashForm

def my_hash_list(request):
    hashes = MyHash.objects.all().order_by('message')
    return render(request, 'my_hash/my_hash_list.html', {'hashes':hashes})

def my_hash_new(request):
    form = MyHashForm()
    return render(request, 'my_hash/edit.html', {'form': form})