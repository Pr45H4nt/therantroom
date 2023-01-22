from idiosaneapp.models import Article , Comment , Subject
from rest_framework import serializers


class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','Body','date_added']

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'