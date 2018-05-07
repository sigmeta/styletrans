# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
#from trans import transfer
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def picstyle(request):
    context = {}
    #transfer.styletransform(os.path.join(BASE_DIR, "trans/models/cubist.ckpt-done"), os.path.join(BASE_DIR, "trans/img/0.jpg"))
    os.system("python trans/eval.py --model_file trans/models/cubist.ckpt-done --image_file trans/img/0.jpg --res_file r.jpg")
    #context['imgfile']="generated/r.jpg"
    return render(request, 'hello.html', context)