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
    ideas = Idea.objects.all()

    # num = 0
    # for idea in ideas:
    #     if devtool.name == idea.dev:
    #         num = idea.id
    #         break
    context = {
        "devtool": devtool,
        "ideas":ideas,
    }

    return render(request, template_name="dev_detail.html", context=context)

def dev_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        description = request.POST["description"]

        DevTool.objects.create(name=name, kind=kind, description=description)

        return redirect("/dev/list")

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
        return redirect("/dev/list") 

# *****************************************************************
def idea_list(request):
    sort = request.GET.get('sort','None')
    if sort == 'last':
        ideas = Idea.objects.all().order_by('created_at')
    elif sort == 'first':
        ideas = Idea.objects.all().order_by('-created_at')
    elif sort == 'title':
        ideas = Idea.objects.all().order_by('title')
    else:
        ideas = Idea.objects.all().order_by('title')
    context = {
        "ideas":ideas
    }
    return render(request, template_name="idea_list.html", context=context)

def idea_detail(request, id):
    idea = Idea.objects.get(id=id) 
    devtools = DevTool.objects.all()
    num = 0
    for devtool in devtools:
        if devtool.name == idea.dev:
            num = devtool.id
            break
    context = {
        "idea": idea,
        "num":num
    }
    return render(request, template_name="idea_detail.html", context=context)

def idea_create(request):
    devtools = DevTool.objects.all()
    # dev_list = []

    # for k in devtools:
    #     dev_list.append(str(k.name))

    # print(dev_list)

    context = {
        # "dev_list":dev_list
        "devtools":devtools
    }

    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
        content = request.POST["content"]
        interest= request.POST["interest"]
        dev = request.POST["dev"]
        Idea.objects.create(title=title, photo=req_photo, content=content, interest=interest, dev=dev)

        return redirect("/")

    return render(request, template_name="idea_create.html", context=context)

def idea_update(request, id):
    devtools = DevTool.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        interest= request.POST["interest"]

        Idea.objects.filter(id=id).update(title=title, content=content, interest=interest)

        return redirect(f"/idea/detail/{id}")

    idea = Idea.objects.get(id=id)
    context = {
        "idea": idea,
        "devtools":devtools
    }
    return render(request, template_name="idea_edit.html", context=context)

def idea_delete(request, id):
    if request.method == "POST":
        Idea.objects.filter(id=id).delete()
        return redirect("/") 