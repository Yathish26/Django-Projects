from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
import math
from service.models import Blogs
from news.models import News
from django.db.models import Q
from tweet.models import Tweet

def home(request):
    data = {
        'title':'Homepage',
        'user':'Yathish',
    }
    
    return render(request,'home.html',data) 

def homedirect(request):
    return redirect('/')
    

def aboutus(request):
    data = {
        'title':'About Us',
        'user':'Yathish',
    }
    return render(request,'aboutus.html',data)

def contactus(request):
    data = {
        'title':'Contact',
        'user':'Yathish',
    }
    return render(request,'contactus.html',data)

def userform(request):
    data = {
        'title':'User Form',
        'user':'Yathish',
        'output':0
    }
    try:
        if request.method=='POST':
            n1 = eval(request.POST['num1'])    
            n2 = eval(request.POST['num2'])     
            data['output']=n1+n2
    except:
        pass
    return render(request,'userform.html',data)

def calculator(request):
    data = {
        'title':'Calculator',
        'user':'Yathish',
    }
    c=""
    try:
        if request.method =='POST':
            keys = ['num1','num2']
            for key in keys:
                if request.POST.get(key) == '':
                    data['error']=True
                    return render(request,'calculator.html',data)
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr == '+':
                c=n1+n2
            elif opr == '-':
                c=n1-n2
            elif opr == '*':
                c=n1*n2
            elif opr== '/':
                c=n1/n2

    except:
        c = "Invalid Operation" 
    data['result']= c 
    return render(request,'calculator.html',data)


def random(request,content):
    data = {
        'title':'Calculator',
        'user':'Yathish',
        'id':content
    }
    return render(request,'random.html',data)


def evenodd(request):
    data = {
        'title':'Even or Odd',
        'user':'Yathish',
    }
    c=''
    if request.method =='POST':
        if request.POST.get("num1")=='':
            data['error']=True
            return render(request,'evenodd.html',data)
    
        n1=eval(request.POST.get("num1"))
        if n1%2==0:
            c="This is Even Number"
        else:
            c="This is an Odd Number"
        
    data['answer']=c
    return render(request,'evenodd.html',data)


def marksheet(request):
    data = {
        'title':'Marksheet',
        'user':'Yathish',
        'answer':0
    }
    c=''
    if request.method == 'POST':
        keys=['m1','m2','m3','m4','m5','m6']
        for key in keys:
            if request.POST.get(key)=='':
                data['error']=True
                return render(request,'marksheet.html',data)
        
        m1=eval(request.POST.get('m1'))
        m2=eval(request.POST.get('m2'))
        m3=eval(request.POST.get('m3'))
        m4=eval(request.POST.get('m4'))
        m5=eval(request.POST.get('m5'))
        m6=eval(request.POST.get('m6'))
        data['total']=m1+m2+m3+m4+m5+m6
        data['percentage']= round(data['total']/150*100,2)
        if data['percentage'] >= 95:
            r="Distinction"
        elif data['percentage'] >= 80:
            r="First Class"
        elif data['percentage'] >= 70:
            r="Second Class"
        elif data['percentage'] >= 35:
            r="Third Class"
        else:
            r="Failed"
        data['result']= r
    return render(request,'marksheet.html',data)

def blogs(request):
    data= {
        'user':'Yathish',
        'title':'Blogs Panel'
    }
    blogdata = Blogs.objects.all().order_by('-id')
    if request.method == 'GET':
        so = request.GET.get("searchkey")
        if so != None:
            blogdata = Blogs.objects.filter(Q(Title__icontains=so)|Q(Category__icontains=so)|Q(Description__icontains=so))
    data['blogdata']=blogdata
    return render(request,'blogs.html',data)

def blogdetail(request,blogdetail):
    data = {
        'user':'Yathish',
        'title':'Blog'
    }
    blogdetaildata = Blogs.objects.get(slugdata=blogdetail)
    data['blogdata']=blogdetaildata
    return render(request,'blogdetail.html',data)

def blogcreate(request):
    data ={
        'user':'Yathish',
        'title':'Create Blog'
    }
    if request.method == 'POST':    
        title=request.POST.get('Title')
        category = request.POST.get('Category')
        description = request.POST.get('Description')
        photo = request.FILES.get('Photo')
        if not category:
            data['categoryerror']=True
        elif not title:
            data['titleerror']=True
        elif not description:
            data['descriptionerror']=True
        elif not title and not category and not description:
            data['inputerror']=True
        elif title and category and description:
            sword = Blogs(Title=title,Category=category,Description=description,Photos=photo)
            sword.save()
            return redirect('/blogs/')
    return render(request,'blogcreate.html',data)

def news(request):
    data = {
        'user':'Yathish',
        'title':'News'
    }
    newsdata = News.objects.all().order_by('-id')
    if request.method == "GET":
        st = request.GET.get('searchkey')
        if st !=None:
            newsdata = News.objects.filter(Q(news_title__icontains=st) | Q(news_description__icontains=st))
    data['newsdata']=newsdata
    return render(request,'news.html',data)

def newsdetails(request,maq):
    data = {
        'user':'Yathish',
        'title':'News Headlines'
    }
    newsdata = News.objects.get(news_slug=maq)
    data['ndetails']=newsdata
    return render(request,'newsdetails.html',data)

def newscreate(request):
    data = {
        'user':'Yathish',
        'title':'Create News'
    }
    if request.method == 'POST':
        title=request.POST.get('newstitle')
        description=request.POST.get('newsdescription')
        photo=request.FILES.get('photo')
        category=request.POST.get('newscategory')
        if not title and not description and not category:
            data['inputerror'] = True
        elif not title:
            data['titleerror'] = True
        elif not description:
            data['descriptionerror'] = True
        elif not category:
            data['categoryerror'] = True

        if title and description and category:
            newsupload = News(
                news_title=title,
                news_description=description,
                news_image=photo,
                news_category=category
            )
            newsupload.save()
            return redirect('/news/')
    return render(request,'newscreate.html',data)

def topnews(request):
    data = {
        'user':'Yathish',
        'title':'Top News'
    }
    return render(request,'News/topnews.html',data)

def business(request):
    data = {
        'user':'Yathish',
        'title':'Business'
    }
    return render(request,'News/business.html',data)

def technology(request):
    data = {
        'user':'Yathish',
        'title':'Technology'
    }
    return render(request,'News/technology.html',data)

def sports(request):
    data = {
        'user':'Yathish',
        'title':'Sports'
    }
    return render(request,'News/sports.html',data)

def entertainment(request):
    data = {
        'user':'Yathish',
        'title':'Entertainment'
    }
    return render(request,'News/entertainment.html',data)

def health(request):
    data = {
        'user':'Yathish',
        'title':'Health'
    }
    return render(request,'News/health.html',data)

def science(request):
    data = {
        'user':'Yathish',
        'title':'Science'
    }
    return render(request,'News/science.html',data)

def politics(request):
    data = {
        'user':'Yathish',
        'title':'Politics'
    }
    return render(request,'News/politics.html',data)

def education(request):
    data = {
        'user':'Yathish',
        'title':'Education'
    }
    return render(request,'News/education.html',data)

def automobiles(request):
    data = {
        'user':'Yathish',
        'title':'Automobiles'
    }
    return render(request,'News/automobiles.html',data)

def lifestyle(request):
    data = {
        'user':'Yathish',
        'title':'Lifestyle'
    }
    return render(request,'News/lifestyle.html',data)

def crime(request):
    data = {
        'user':'Yathish',
        'title':'Crime'
    }
    return render(request,'News/crime.html',data)

def agriculture(request):
    data = {
        'user':'Yathish',
        'title':'Agriculture'
    }
    return render(request,'News/agriculture.html',data)

def tweet(request):
    data = {
        'user':'Yathish',
        'title':'Tweet'
    }
    tweetdata = Tweet.objects.all().order_by("-id")
    if request.method == "GET":
        so = request.GET.get("searchkey")
        if so!= None:
            tweetdata=Tweet.objects.filter(Q(username__icontains=so)|Q(tweet__icontains=so))  
    data['tweetdata']=tweetdata
    
    if request.method == "POST":
        username = request.POST.get("username")
        tweet = request.POST.get("tweet")
        if not username and not tweet:
            data['usernameandtweeterror'] = True
        elif username and not tweet:
            data['username_yes_notweet'] = True
        elif not username and tweet:
            data['username_no_yestweet'] = True
        elif username and tweet:
            data['usernameandtweetyes'] = True
        else:
           pass

        if not data.get('usernameandtweeterror') and not data.get('username_yes_notweet') and not data.get('username_no_yestweet'):
            fetch = Tweet(username=username, tweet=tweet)
            fetch.save()  
            return redirect('/tweets/')      
    return render(request,'tweets.html',data)