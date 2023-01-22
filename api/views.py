from .serializers import Articleserializer , Article , Commentserializer , Categoryserializer , Subject
from rest_framework import generics , permissions

class Articlelist(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Article.objects.get(pk = self.kwargs['pk']).comments.all()
    serializer_class = Commentserializer

    def perform_create(self, serializer):
        serializer.save(post= Article.objects.get(pk=self.kwargs['pk']))

class Categorylist(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = Categoryserializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]