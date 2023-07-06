"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from movie_app.views import DirectorListAPIView, DirectorDetailAPIView, MovieListAPIView,MovieDetailAPIView,ReviewListAPIView,ReviewDetailAPIView,MovieReviewListAPIView

 

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    # ...
    path('api/v1/directors/', DirectorListAPIView.as_view(), name='director-list'),
    path('api/v1/directors/<int:id>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('api/v1/movies', MovieListAPIView.as_view(), name='movie-list'),
    path('api/v1/movies/<int:id>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('api/v1/reviews', ReviewListAPIView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('api/v1/movies/reviews/', MovieReviewListAPIView.as_view(), name='movie-review-list'),
    path('api/v1/directors/', DirectorListAPIView.as_view(), name='director-list'),
    # ...
]

from django.urls import path
from movie_app.views import DirectorListCreateAPIView,MovieListCreateAPIView,ReviewListCreateAPIView
from movie_app.views import DirectorRetrieveUpdateDestroyAPIView,MovieRetrieveUpdateDestroyAPIView,ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    # ...
    path('api/v1/directors/', DirectorListCreateAPIView.as_view(), name='director-list'),
    path('api/v1/directors/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view(), name='director-detail'),
    path('api/v1/movies', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('api/v1/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
    path('api/v1/reviews', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
    # ...
]

from django.urls import path
from movie_app.views import DirectorListAPIView, DirectorCreateAPIView

urlpatterns = [
    # ...
    path('api/v1/directors/', DirectorListAPIView.as_view(), name='director-list'),
    path('api/v1/directors/create/', DirectorCreateAPIView.as_view(), name='director-create'),
    # ...
]
