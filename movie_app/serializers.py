from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("id", "name")

    def validate_name(self, value):
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

  
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

    def validate_duration(self, value):
        if value < 0:
            raise ValidationError("Длительность фильма должна быть положительным числом.")
        return value
    
    def validate_id(self, value):
        try:
            movie = Movie.objects.get(id=value)
        except Movie.DoesNotExist:
            raise ValidationError("Фильм с указанным идентификатором не существует.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ("id", "text", "movie", "stars")

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise ValidationError("Рейтинг отзыва должен быть числом от 1 до 5.")
        return value
    
    def validate_id(self, value):
        try:
            review = Review.objects.get(id=value)
        except Review.DoesNotExist:
            raise ValidationError("Отзыв с указанным идентификатором не существует.")
        return value
    
    
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "reviews", "rating")


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ("id", "name", "movies_count")


from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
