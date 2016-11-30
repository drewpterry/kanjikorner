from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import * 


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SetsViewSet(viewsets.ModelViewSet):
    queryset = Sets.objects.filter(master_order=1)
    serializer_class = SetsSerializer

class WordsViewSet(viewsets.ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

class WordMeaningsViewSet(viewsets.ModelViewSet):
    queryset = WordMeanings.objects.all()
    serializer_class = WordMeaningsSerializer

class KnownWordsViewSet(viewsets.ModelViewSet):
    queryset = KnownWords.objects.all()
    serializer_class = KnownWordsSerializer
