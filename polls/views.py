from django.shortcuts import render, get_object_or_404
from .models import Poll
from .models import Article
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer

# Create your views here.

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {'results': list(polls.values('question', 'created_by__username','pub_date'))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {'results': {
        'question': poll.question,
        'created_by': poll.created_by_username,
        'pub_date': poll.pub_date
    }}
    return JsonResponse(data)


@csrf_exempt

def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        # check if the data is valid

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)