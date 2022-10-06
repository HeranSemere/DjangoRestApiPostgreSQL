from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from mindplex.models import Article
from mindplex.models import Interaction
from mindplex.models import RecommendationConfiguration
 

from mindplex.serializers import ArticleSerializer
from mindplex.serializers import InteractionSerializer
from mindplex.serializers import RecommendationConfigurationSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def articles_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        articles_serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(articles_serializer.data, safe=False)
    elif request.method == 'POST':
        article_data = JSONParser().parse(request)
        article_serializer = ArticleSerializer(data=article_data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Article.objects.all().delete()
        return JsonResponse({'message': '{} articles were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def articles_detail(request, pk):
    # find article by pk (id)
    try: 
        article = Article.objects.get(pk=pk)
        if request.method == 'GET': 
            article_serializer = ArticleSerializer(article) 
            return JsonResponse(article_serializer.data)
        elif request.method == 'PUT': 
            article_data = JSONParser().parse(request) 
            article_serializer = ArticleSerializer(article, data=article_data) 
            if article_serializer.is_valid(): 
                article_serializer.save() 
                return JsonResponse(article_serializer.data) 
            return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            article.delete() 
            return JsonResponse({'message': 'Article was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Article.DoesNotExist: 
        return JsonResponse({'message': 'The article does not exist'}, status=status.HTTP_404_NOT_FOUND) 


@api_view(['GET', 'POST', 'DELETE'])
def recommendationconfiguration_list(request):
    if request.method == 'GET':
        recommendationconfiguration = RecommendationConfiguration.objects.all()
        recommendationconfiguration_serializer = RecommendationConfigurationSerializer(recommendationconfiguration, many=True)
        return JsonResponse(recommendationconfiguration_serializer.data, safe=False)
    elif request.method == 'POST':
        recommendationconfiguration_data = JSONParser().parse(request)
        recommendationconfiguration_serializer = RecommendationConfigurationSerializer(data=recommendationconfiguration_data)
        if recommendationconfiguration_serializer.is_valid():
            recommendationconfiguration_serializer.save()
            return JsonResponse(recommendationconfiguration_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(recommendationconfiguration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = RecommendationConfiguration.objects.all().delete()
        return JsonResponse({'message': '{} recommendation configurations were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def recommendationconfiguration_detail(request, pk):
    try: 
        recommendationconfiguration = RecommendationConfiguration.objects.get(pk=pk)
        if request.method == 'GET': 
            recommendationconfiguration_serializer = RecommendationConfigurationSerializer(recommendationconfiguration) 
            return JsonResponse(recommendationconfiguration_serializer.data)
        elif request.method == 'PUT': 
            recommendationconfiguration_data = JSONParser().parse(request) 
            recommendationconfiguration_serializer = RecommendationConfigurationSerializer(recommendationconfiguration, data=recommendationconfiguration_data) 
            if recommendationconfiguration_serializer.is_valid(): 
                recommendationconfiguration_serializer.save() 
                return JsonResponse(recommendationconfiguration_serializer.data) 
            return JsonResponse(recommendationconfiguration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            recommendationconfiguration.delete() 
            return JsonResponse({'message': 'Recommendation Configuration was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Article.DoesNotExist: 
        return JsonResponse({'message': 'The Recommendation Configuration does not exist'}, status=status.HTTP_404_NOT_FOUND)  

    
@api_view(['GET', 'POST', 'DELETE'])
def interactions_list(request):
    if request.method == 'GET':
        interactions = Interaction.objects.all()
        interactions_serializer = InteractionSerializer(interactions, many=True)
        return JsonResponse(interactions_serializer.data, safe=False)
    elif request.method == 'POST':
        interaction_data = JSONParser().parse(request)
        interaction_serializer = InteractionSerializer(data=interaction_data)
        if interaction_serializer.is_valid():
            interaction_serializer.save()
            return JsonResponse(interaction_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Interaction.objects.all().delete()
        return JsonResponse({'message': '{} interactions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def interactions_detail(request, pk):
    try: 
        interaction = Interaction.objects.get(pk=pk)
        if request.method == 'GET': 
            interaction_serializer = InteractionSerializer(interaction) 
            return JsonResponse(interaction_serializer.data)
        elif request.method == 'PUT': 
            interaction_data = JSONParser().parse(request) 
            interaction_serializer = InteractionSerializer(interaction, data=interaction_data) 
            if interaction_serializer.is_valid(): 
                interaction_serializer.save() 
                return JsonResponse(interaction_serializer.data) 
            return JsonResponse(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            interaction.delete() 
            return JsonResponse({'message': 'Interaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Article.DoesNotExist: 
        return JsonResponse({'message': 'The interaction does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    
    
@api_view(['GET'])
def recommendation(request, pk):
    if request.method == 'GET':
        recommendationconfiguration = RecommendationConfiguration.objects.all()
        recommendationconfiguration_serializer = RecommendationConfigurationSerializer(recommendationconfiguration, many=True)
        return JsonResponse(recommendationconfiguration_serializer.data, safe=False)
 
