from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Director
from .models import Movie
from .serializers import DirectorSerializer
from .serializers import MovieSerializer
from .models import Review
from .serializers import ReviewSerializer
from django.db.models import Avg
from django.db.models import Count
from rest_framework.views import APIView


class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class MovieReviewListAPIView(generics.ListAPIView):
    queryset = Movie.objects.annotate(rating=Avg('review__stars'))
    serializer_class = MovieSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_reviews'] = True
        return context

class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movie'))
    serializer_class = DirectorSerializer

class DirectorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class DirectorCreateAPIView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer