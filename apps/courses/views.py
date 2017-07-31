# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages

def index(request):
    context = {
    "courses": Course.objects.all()}
    return render(request, 'courses/index.html', context)

def create(request):
    if len(Course.objects.filter(name=request.POST['name'])) > 0:
        messages.error(request, 'Already a course by that name!')
    else:
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(description=request.POST['description'], course = course)
        messages.success(request, 'Adding a course!')
    return redirect("/")

def comment(request, id):
    context = {
        "course" : Course.objects.get(id=id),
        "comment" : Comment.objects.filter(course=id)
    }
    return render(request, "courses/comment.html", context)

def add_comment(request, id):
    course = Course.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], course = course)
    return redirect('/comment/'+id)

def delete(request, id):
    context = {
        "course" : Course.objects.get(id=id),
    }
    return render(request, "courses/destroy.html", context)

def delete_confirm(request, id):
    Course.objects.filter(id=id).delete()
    messages.success(request, 'Removed a course!')
    return redirect("/")
