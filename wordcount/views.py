from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'hithere':'This is me!'})

def boe(request):
    return HttpResponse('<h1><b>Boe Boe poep in je handen en knijp dan toe!</b></h1>')

def count(request):
    text = request.GET['fulltext']
    textarr = text.split()
    worddictionary = {}

    for word in textarr:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            #add to worddictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),key = operator.itemgetter(1), reverse = True)
    return render(request,'count.html',{'title':'Word Counts:',
                                        'tekst':text,'count':len(textarr),
                                        'sortedwords':sortedwords})

def about(request):
    text = 'Wordcount laat je zien hoeveel worden er in een stukje tekst zitten en hoevaak deze woorden in de tekst voorkomen'

    return render(request,'about.html',{'title':'About Wordcount:',
                                        'text': text})
