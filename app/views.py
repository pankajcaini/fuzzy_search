from django.shortcuts import render
from django.http import JsonResponse
from thefuzz import process, fuzz


words = [
    'apple','apply','application','pat','cat','bat','pen','pack','lack','jack',"rekhachithram","mr nobody","receive","luck","look",
    "mug","centimetre","coordination","inception","intercept","bowl","ball","iphone","phone","kill","pill","still","wall","stretch","spiderman","postman",
    "dear","bear","harry potter","global","library","axieva"
]


def home(request):
    if request.method == 'GET':
        return render(request, "home.html")
    

def search_similar(request, sterm):
    swords = process.extract(sterm, words, limit=4, scorer=fuzz.partial_ratio)

    matched_word = []
    for word in swords:
        w,c = word
        if c >=70:
            matched_word.append(w)

    return JsonResponse({"suggestions":matched_word})
