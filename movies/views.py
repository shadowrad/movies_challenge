from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from core.permissions import ListDefaultPermissions
from movies.models import Movie, Person, PersonAlias
from movies.serializers import MovieSerializer, PersonSerializer, PersonAliasSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [ListDefaultPermissions]


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [ListDefaultPermissions]


class PersonAliasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PersonAlias.objects.all()
    serializer_class = PersonAliasSerializer
    permission_classes = [permissions.IsAdminUser]

