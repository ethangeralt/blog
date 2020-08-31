from django.shortcuts import HttpResponse, redirect, render
from amol_blog.models import Slideshow
from amol_blog.models import Latest
from amol_blog.models import Comment, Messages, Subscribers, Profile_pic
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404

#This section is for Home, Here Data from Slidshow and Latest Table Coming
def home(request):
    slids = Slideshow.objects.all()
    burns = Latest.objects.all()
    context = {
        'slids' : slids,
        'burns' : burns
    }
    if request.method == 'POST':
        subscribe = Subscribers()
        subscribe.email = request.POST.get('email_sub')
        subscribe.save()
        messages.success(request, 'Successfully Subscribed')
    
    return render(request, 'index.html', context)
def read_blog(request, id):   
    read_slid = Slideshow.objects.filter(id=id)
    read_late = Latest.objects.filter(id=id)
    comm = Comment.objects.all().filter(post=id)
    comm_latest = Comment.objects.all().filter(post2=id)
    context = {
        'comm': comm,
        'comm_latest' : comm_latest,
        'read_slid' : read_slid,
        'read_late' : read_late,
    }
    if request.method == 'POST':
        comment = Comment()
        comment.post_id = request.POST.get('post_id')
        comment.post2_id = request.POST.get('post2_id')
        comment.name = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.comment = request.POST.get('comment')
        comment.save()
        return render(request, 'blog_read.html', context, id)
    return render(request, 'blog_read.html', context, id)
def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
       if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username=username, password=password)
          auth.login(request, user)
          messages.success(request, "Successfully LogedIn! Redirecting Home")
          return redirect('home')
          return render(request, 'login.html')
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        messages.success(request, 'Successfully Registered! Redirecting To Login')
        return render(request, 'register.html')
    return render(request, 'register.html')

def search(request):
    if request.method=='GET':
        query= request.GET.get('search')
        if query is not None:
            lookup=Q(title__icontains=query) | Q(short_desc__icontains=query) | Q(id__icontains=query ) | Q(long_dec__icontains=query )
            result_slide = Slideshow.objects.filter(lookup).distinct()
            result_late = Latest.objects.filter(lookup).distinct()
            context = {
                'result_slide' : result_slide,
                'result_late'  : result_late
            }
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html', context)
    return render(request, 'search.html')

def contact_us(request):
    if request.method == 'POST':
        msg = Messages()
        msg.name = request.POST.get('name')
        msg.email = request.POST.get('email')
        msg.msg = request.POST.get('message')
        msg.save()
        messages.success(request, 'Your Query Sent Successfully')
        return render(request, 'page-contact.html')
    return render(request, 'page-contact.html')
 
def bihar_blog_admin_data(request):
    if request.method == "POST":
        title = request.POST['title']
        photo = request.FILES['form__gallery-upload']
        short_desc = request.POST['short_description']
        long_dec = request.POST['long_description']
        date = request.POST['date']
        slide = Slideshow.objects.create(title=title, short_desc=short_desc, long_dec=long_dec, photo=photo)
        messages.success(request, 'Item Added Successfully To Databaase')
        return render(request, 'add-item.html')
    return render(request, 'add-item.html')

def upload(request):
    if request.method == 'POST':
        simple = Slideshow()
        simple.title = request.POST['title']
        simple.short_desc = request.POST['short']
        simple.long_dec = request.POST['long']
        simple.date = request.POST['date']
        simple.photo = request.FILES['photo']
        simple.save()
        return render(request, 'upload.html')
    return render(request, 'upload.html')

def about_us(request):
    return render(request, 'page-about-me.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request, id):
    pro_id = Profile_pic.objects.filter(id=id)
    pro = Profile_pic.objects.filter(pic=id).last()
    context = {
        'pro': pro
    }
    if request.method == 'POST':
        prof = Profile_pic()
        prof.pic_id = request.POST['user_id']
        prof.prof_pic = request.FILES['prof_pic']
        prof.location = request.POST['location']
        prof.bio = request.POST['bio']
        prof.save()
        return render(request, 'profile.html', context, id)
    return render(request, 'profile.html', context, id)


