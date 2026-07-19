from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


@login_required(login_url='login')
def dashboard(request):

    blogs = Blog.objects.filter(author=request.user)

    category_count = Category.objects.filter(
        blog__author=request.user
    ).distinct().count()

    blogs_count = blogs.count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }

    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


@login_required
def posts(request):
    print("Current User:", request.user)

    blogs = Blog.objects.filter(author=request.user).order_by('-created_at')

    print("Blogs found:", blogs.count())

    for blog in blogs:
        print(blog.title, blog.author)

    return render(request, "dashboard/posts.html", {
        "blogs": blogs,
    })

@login_required(login_url='login')
def add_post(request):
    print("View Called")

    if request.method == "POST":
        print("POST Request Received")
        print(request.POST)
        print(request.FILES)

        form = BlogPostForm(request.POST, request.FILES)

        print("Form Valid:", form.is_valid())

        if form.is_valid():
            print("Saving Blog...")

            post = form.save(commit=False)
            post.author = request.user

            post.save()

            print("Saved Successfully:", post.id)

            post.slug = slugify(post.title) + "-" + str(post.id)
            post.save()

            return redirect("posts")

        else:
            print(form.errors)

    form = BlogPostForm()

    return render(request, "dashboard/add_post.html", {"form": form})


@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk, author=request.user)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()

            return redirect('posts')

    else:
        form = BlogPostForm(instance=post)

    return render(request, 'dashboard/edit_post.html', {
        'form': form,
        'post': post,
    })

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')



def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)


def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit_user.html', context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')