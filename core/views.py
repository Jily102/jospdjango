import requests

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MessageForm
from .models import Message


def home(request):
    # retrieve popular post from josblog api
    r = requests.get("https://jospblog.herokuapp.com/api/")
    posts_json = r.json()

    posts = []

    for post in posts_json:
        post_url = post["post_url"]
        post_title = post["title"]
        post_desc = post["descript"]
        post_views = post["post_views"]

        post_info = {
            "post_url": post_url,
            "post_title": post_title,
            "post_desc": post_desc,
            "post_views": post_views,
        }

        posts.append(post_info)

    popular_posts = sorted(posts, key=lambda d: d["post_views"], reverse=True)[:3]

    unreadCount = Message.objects.filter(is_read=False).count()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You message was successfully sent!.')
            return redirect('home')
    else:
        form = MessageForm()

    context = {
        'form': form,
        'unreadCount': unreadCount,
        'popular_posts': popular_posts
    }

    return render(request, 'core/home.html', context)

def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}

    return render(request, 'core/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {
        'message': message,
        'unreadCount': unreadCount
    }
    
    return render(request, 'core/message.html', context)