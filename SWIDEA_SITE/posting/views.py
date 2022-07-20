from django.shortcuts import redirect, render
from .models import DevTool, Idea

# Create your views here.
def dev_list(request):
    devtools = DevTool.objects.all()
    context = {
        "devtools":devtools
    }
    return render(request, template_name="dev_list.html", context=context)

def dev_detail(request, id):
    devtool = DevTool.objects.get(id=id) 
    context = {
        "devtool": devtool,
    }
    return render(request, template_name="dev_detail.html", context=context)

def dev_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        description = request.POST["description"]

        DevTool.objects.create(name=name, kind=kind, description=description)

        return redirect("/")

    context = {}

    return render(request, template_name="dev_create.html", context=context)

def dev_update(request, id):
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        description = request.POST["description"]

        DevTool.objects.filter(id=id).update(name=name, kind=kind, description=description)

        return redirect(f"/dev/detail/{id}")

    devtool = DevTool.objects.get(id=id)
    context = {
        "devtool": devtool
    }
    return render(request, template_name="dev_edit.html", context=context)

def dev_delete(request, id):
    if request.method == "POST":
        DevTool.objects.filter(id=id).delete()
        return redirect("/") 

# *****************************************************************
def idea_list(request):
    ideas = Idea.objects.all()
    context = {
        "ideas":ideas
    }
    return render(request, template_name="idea_list.html", context=context)

def idea_detail(request, id):
    idea = Idea.objects.get(id=id) 
    context = {
        "idea": idea,
    }
    return render(request, template_name="idea_detail.html", context=context)

def idea_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
        content = request.POST["content"]

        Idea.objects.create(title=title, photo=req_photo, content=content)

        return redirect("/")

    context = {}

    return render(request, template_name="idea_create.html", context=context)

def idea_update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        # photo = request.POST["photo"]
        content = request.POST["content"]

        Idea.objects.filter(id=id).update(title=title, content=content)

        return redirect(f"/idea/detail/{id}")

    idea = Idea.objects.get(id=id)
    context = {
        "idea": idea
    }
    return render(request, template_name="idea_edit.html", context=context)

def idea_delete(request, id):
    if request.method == "POST":
        Idea.objects.filter(id=id).delete()
        return redirect("/") 