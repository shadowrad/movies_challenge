from rest_framework import serializers

from movies.models import Movie, Person, PersonAlias


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    roman_year = serializers.CharField()

    class Meta:
        model = Movie
        fields = '__all__'


class PersonAliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonAlias
        fields = ['name']


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    movies_as_actors = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)
    movies_as_directors = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)
    movies_as_producers = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)
    aliases = PersonAliasSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'
