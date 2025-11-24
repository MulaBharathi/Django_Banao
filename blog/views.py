from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

# ---------- DOCTOR: Create Blog ----------
@login_required
def create_blog(request):
    if request.user.user_type != "doctor":
        return redirect("home") # only doctors can access

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES) # gets form data + uploaded image
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # attached logged-in doctor
            blog.save()
            return redirect("doctor_blogs") # redirect to doctor blog list
    else:
        form = BlogForm() # empty form for GET requests

    return render(request, "blog/create_blog.html", {"form": form})

# ---------- DOCTOR: View Own Blogs ----------
@login_required
def doctor_blogs(request):
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, "blog/doctor_blogs.html", {"blogs": blogs})

# ---------- DOCTOR: Edit Blog ----------
@login_required
def edit_blog(request, id):
    blog = BlogPost.objects.get(id=id, author=request.user)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("doctor_blogs")
    else:
        form = BlogForm(instance=blog)

    return render(request, "blog/edit_blog.html", {"form": form})


# ---------- DOCTOR: Delete Blog ----------
@login_required
def delete_blog(request, id):
    blog = BlogPost.objects.get(id=id, author=request.user)
    blog.delete()
    return redirect("doctor_blogs")

# ---------- PATIENT: Category-wise Blog List ----------
def patient_blog_list(request):
    categories = ["mental", "heart", "covid", "immunization"]
    data = {}

    for cat in categories:
        posts = BlogPost.objects.filter(category=cat, is_draft=False)
        data[cat] = posts

    return render(request, "blog/patient_blog_list.html", {"data": data})

