from rest_framework import serializers
from .models import Director,Movie,Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')
    def validate_name(self,value):
        if len(value) < 2:
            raise ValidationError("Имя режиссера должно содержать не менее 2 символов.")
        return value

    def validate_id(self, value):
        try:
            director = Director.objects.get(id=value)
        except Director.DoesNotExist:
            raise ValidationError("Режиссер с указанным идентификатором не существует.")
        return value

    

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ('id', 'text', 'movie' , 'stars')


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'reviews', 'rating')


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')
