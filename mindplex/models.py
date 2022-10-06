from django.db import models

# Create your models here.
class Article(models.Model):
    UniqueID = models.IntegerField(primary_key = True)
    authorId = models.CharField(max_length=70, blank=False, default='')
    autherResidence = models.CharField(max_length=200,blank=False, default='')
    communityId = models.CharField(max_length=70, blank=False, default='')
    content = models.TextField(blank=False, default='')
    contentId = models.CharField(max_length=70, blank=False, default='')
    source = models.CharField(max_length=70, blank=False, default='')
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=70, blank=False, default='')
    url = models.CharField(max_length=70, blank=False, default='')
    
    
class Interaction(models.Model):
    UniqueID = models.IntegerField(primary_key = True)
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE)
    communityId = models.CharField(max_length=70, blank=False, default='')
    eventType = models.BigIntegerField()
    location = models.CharField(max_length=70, blank=False, default='')
    source = models.BigIntegerField()
    timestamp = models.DateTimeField()
    userId = models.CharField(max_length=70, blank=False, default='')
    class Meta:
        db_table = 'Interaction'
        constraints = [
            models.UniqueConstraint(fields=['userId', 'eventType', 'articleId'], name='unique Interaction')
        ]        
        
class RecommendationConfiguration(models.Model):
    CommunityID = models.IntegerField(primary_key = True)
    highQuality = models.FloatField()
    pattern = models.FloatField()
    popularity = models.FloatField()
    random = models.FloatField()
    timeliness = models.FloatField()
    class Meta:
       ordering = ['-highQuality', '-random', '-pattern',  '-popularity','-timeliness']
    