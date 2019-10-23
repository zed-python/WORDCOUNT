from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    
    return render( request ,'home.html')
    
def count(request):
    text = request.GET['text']
    wordcount = text.split()
    
    worddictionary = {}

    for word in wordcount :
        if  word in worddictionary:
            #increse
            worddictionary[word] += 1 
        else:
            worddictionary[word] = 1     
    totalsorted = sorted(worddictionary.items() ,key = operator .itemgetter(1), reverse= True)
    
    return render( request ,'count.html',{'text':text,'counter':len(wordcount),'totalsorted':totalsorted})
def about(request):
    return render ( request , 'about.html')