from django.shortcuts import redirect, render
from .models import DevTool

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