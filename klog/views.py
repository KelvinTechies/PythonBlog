from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import os
# Create your views here.

# @login_required(login_url='login')
def home(request):
    blogs = Blog.objects.all().order_by('-Date_Created')[0:4]
    posts = PostCategory.objects.all().order_by('-Date_Created')[0:3]
    Allposts = PostCategory.objects.all()
    threeblogs = Blog.objects.all().order_by('-Date_Created')[0:3]
    singleView = Blog.objects.all().order_by('-Date_Created')[0]
    singlepost = PostCategory.objects.all().order_by('-Date_Created')[0]
    # .order_by('-pub_date')[0:3]
    context = {'blogs':blogs, 'posts':posts, 'Allposts':Allposts, 'threeblogs': threeblogs, 'singleView': singleView, 'singlepost': singlepost}
    return render(request, 'klog/home.html', context)

@login_required(login_url='login')
def createblog(request):
    if request.method=='POST':
        blog = Blog()
        blog.Author = request.POST.get('author')
        blog.Title = request.POST.get('title')
        blog.Category = request.POST.get('category')
        blog.Description = request.POST.get('description')
        if len(request.FILES) != 0:
           img = request.FILES['img']
        blog.save()
        return redirect('viewpost')
            # context = {}     
    return render(request, 'klog/create-post.html')

@login_required(login_url='login')
def createpost(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            img = request.FILES['img']
        author = request.POST.get('author')
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        # print(author, title, category, description)
        newpost = PostCategory.objects.create(Author=author,
            Title=title, Category=category,
            Description=description)
        newpost.save()
        return redirect('viewblog')
                  
    return render(request, 'klog/klogpost/create-blog.html')
    
@login_required(login_url='login')
def viewpost(request):
    posts = PostCategory.objects.all()
    context = {'posts':posts}
    return render(request, 'klog/klogpost/view-blog.html', context)

@login_required(login_url='login')
def viewblog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'klog/view-post.html', context)

@login_required(login_url='login')
def editpost(request, pk):
    post = PostCategory.objects.get(id=pk)

    if request.method == 'POST':
        img = request.FILES['img']
        
        # if len(request.FILES) !=0:
        #     if len(post.Image)> 0:
        #        os.remove(post.Image.path)
        #        post.Image = request.FILES['img']
        # forms = PostCategoryForm(request.POST, instance=post)
        post.Author = request.POST.get('author')
        post.Title = request.POST.get('title')
        post.Category = request.POST.get('category')
        post.Description = request.POST.get('description')
        post.Image =  request.FILES['img']
        post.save()
        return redirect('viewblog')
    context = {'post':post}
    return render(request, 'klog/klogpost/edit-blog.html', context)



@login_required(login_url='login')
def editblog(request, pk):
    blog = Blog.objects.get(id=pk)

    # forms  = BlogForm(instance=blogs)
    if request.method =='POST':
        img = request.FILES['img']
            
            # if len(request.FILES) !=0:
            #    if len(blog.Image)> 0:
            #       os.remove(blog.Image.path)
        blog.Image = request.FILES['img']
        blog.Author =request.POST.get('author')
        blog.Title = request.POST.get('title')
        blog.Category = request.POST.get('category')
        blog.Description = request.POST.get('description')
        blog.save()
        return redirect('/view-post')
    context = {'blog':blog}
    return render(request, 'klog/edit-post.html', context)

@login_required(login_url='login')
def deleteblog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('/view-post')
@login_required(login_url='login')
def deletepost(request, pk):
    deletepost = PostCategory.objects.get(id=pk)
    if request.method == 'POST':
        deletepost.delete()
        return redirect('/view-blog')

@login_required(login_url='login')
def description(request, pk):
    post = PostCategory.objects.get(id=pk)
    blogs = Blog.objects.all()
    context = {'post':post, 'blogs':blogs}
    return render(request, 'klog/klogpost/description.html', context)

@login_required(login_url='login')
def details(request, pk):
    post = PostCategory.objects.get(id=pk)
    posts = PostCategory.objects.all().order_by('-Date_Created')[0:3]
    blogs = Blog.objects.all().order_by('-Date_Created')[0:3]
    pcomm = CommentPost.objects.all().filter(postCategory=PostCategory.objects.get(id=pk))
    print('nbjkgb')
    print(pcomm)
    context = {'post':post, 'posts': posts, 'blogs':blogs, 'pcomm':pcomm}
    return render(request, 'klog/klogpost/detail.html', context)

@login_required(login_url='login')
def detailsblog(request, pk):
    post = Blog.objects.get(id=pk)
    posts = Blog.objects.all().order_by('-Date_Created')[0:3]
    blogs = PostCategory.objects.all().order_by('-Date_Created')[0:3]
    b=Blog.objects.get(id=pk)
    bcomm = BlogComment.objects.all().filter(Blog=Blog.objects.get(id=pk))
    # print('nbjkgb')
    # print(bcomm)
    # context = {'bcomm':bcomm}
    context = {'post':post, 'posts': posts, 'blogs':blogs,'bcomm':bcomm}
    return render(request, 'klog/blog-details.html', context)

@login_required(login_url='login')
def Education(request):
    blog = Blog.objects.all()
    blogs = blog.filter(Category='Education')
    posts = PostCategory.objects.all().order_by('-Date_Created')[0:3]
    singleView = Blog.objects.all().order_by('-Date_Created')[0]
    AllBogs = Blog.objects.all().order_by('-Date_Created')[0:3]
    Allposts = PostCategory.objects.all()
    
    context = {'blogs':blogs, 'posts':posts, 'singleView': singleView, 'AllBogs': AllBogs, 'Allposts':Allposts}
    
    return render(request, 'klog/Education.html', context)
    
@login_required(login_url='login')
def sports(request):
    blog = PostCategory.objects.all()
    blogs = blog.filter(Category='Football')
    posts = Blog.objects.all().order_by('-Date_Created')[0:3]
    singleView = PostCategory.objects.all().order_by('-Date_Created')[0]
    AllBogs = Blog.objects.all().order_by('-Date_Created')[0:3]
    Allposts = PostCategory.objects.all().order_by('-Date_Created')[0:3]
    
    context = {'blogs':blogs, 'posts':posts, 'singleView': singleView, 'AllBogs': AllBogs, 'Allposts':Allposts}
    return render(request, 'klog/sport.html', context)

@login_required(login_url='login')
def blogcomment(request, pk):
    blog=Blog.objects.get(id=pk)
    
    comment=BlogComment()
    if request.method == 'POST':
        comment.name = request.POST.get('name')
        comment.Blog=blog
        comment.Body=request.POST.get('desc')
        print(comment)
        
        comment.save()
    # print(comment)

    # context = {'comment':comment}
    
    return redirect('/')
    # return render(request, 'klog/blog-details.html', context)
    #
    # return HttpResponseRedirect(request.path_info())
@login_required(login_url='login')
def comment(request, pk):
    post_comm=PostCategory.objects.get(id=pk)
    
    comment=CommentPost()
    if request.method == 'POST':
        comment.name = request.POST.get('name')
        comment.postCategory=post_comm
        comment.Body=request.POST.get('desc')
        print(comment)
        
        comment.save()

    # context = {'comment':comment}
    
    return redirect('/')
        

# def Sports(request):
#     blog = Blog.objects.all()
#     blogs = blog.filter(Category='Sport')
#     posts = PostCategory.objects.all()
#     singleView = Blog.objects.all().order_by('-Date_Created')[0]
#     singlepost = PostCategory.objects.all().order_by('-Date_Created')[0]
#     # print(post)
#     context = {'blogs':blogs, 'posts':posts, 'singleView': singleView, 'singlepost': singlepost}
    
#     return render(request, 'klog/Sport.html', context)
# @login_required(login_url='login')
def loginin(request):
    # logout(request)
    if request.method== 'POST':
        print(request.POST)
    return render(request, 'klog/login.html')

@login_required(login_url='login')
def LoggingOut(request):
    logout(request)
    return redirect('logginin')