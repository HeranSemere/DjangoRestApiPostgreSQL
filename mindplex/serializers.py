from rest_framework import serializers 
from mindplex.models import Article
from mindplex.models import Interaction
from mindplex.models import RecommendationConfiguration

class ArticleSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Article
        fields = ('UniqueID',
                  'authorId',
                  'autherResidence',
                  'communityId',
                  'content',
                  'contentId',
                  'source',
                  'timestamp',
                  'title',
                  'url'
                 )

class InteractionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Interaction
        fields = ('UniqueID',
                  'communityId',
                  'eventType',
                  'location',
                  'source',
                  'timestamp',
                  'userId',
                  'articleId'
                  
                 )
        
        
class RecommendationConfigurationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RecommendationConfiguration
        fields = ('CommunityID',
                  'highQuality',
                  'pattern',
                  'popularity',
                  'random',
                  'timeliness'
                 )
        
 