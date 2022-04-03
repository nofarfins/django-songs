from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def performance_list(request):
    if request.method == 'GET':
        all_performance = Performance.objects.all()
        if 'filter_amount' in request.GET and request.GET['filter_amount']:
            all_performance = all_performance.filter(Amount_of_views__icontains=request.GET['filter_amount'])
        if 'filter_singer' in request.GET and request.GET['filter_singer']:
            all_performance = all_performance.filter(singer__name__icontains=request.GET['filter_singer'])
        if 'filter_song' in request.GET and request.GET['filter_song']:
            all_performance = all_performance.filter(song__name__icontains=request.GET['filter_song'])

        serializer = PerformanceSerializer(all_performance, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        song = Song.objects.get(pk=request.data['song'])
        singer = Artist.objects.get(pk=request.data['singer'])

        performance = Performance.objects.create(link=request.data['link'], song=song, singer=singer, Amount_of_views=request.data['Amount_of_views'])

        serializer = PerformanceSerializer(performance)

        if performance.id is not None:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def performance_details(request, pk):
    print("hey")

    try:
        performance = Performance.objects.get(pk=pk)
    except Performance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerformanceSerializer(performance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PerformanceSerializerUpdate(performance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        performance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        all_songs = Song.objects.all()
        if 'filter_name' in request.GET and request.GET['filter_name']:
            all_songs = all_songs.filter(name__icontains=request.GET['filter_name'])
        if 'filter_lyrics' in request.GET and request.GET['filter_lyrics']:
            all_songs = all_songs.filter(lyrics__icontains=request.GET['filter_lyrics'])
        if 'filter_singer' in request.GET and request.GET['filter_singer']:
            all_songs = all_songs.filter(singer__name__icontains=request.GET['filter_singer'])
        if 'filter_writer' in request.GET and request.GET['filter_writer']:
            all_songs = all_songs.filter(song_writer__name__icontains=request.GET['filter_writer'])
        if 'filter_composer' in request.GET and request.GET['filter_composer']:
            all_songs = all_songs.filter(song_composer__name__icontains=request.GET['filter_composer'])


        serializer = SongSerializer(all_songs, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def song_details(request, pk):

    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        all_artists = Artist.objects.all()

        if 'filter_name' in request.GET and request.GET['filter_name']:
            all_artists = all_artists.filter(name__icontains=request.GET['filter_name'])
        if 'filter_age' in request.GET and request.GET['filter_age']:
            all_artists = all_artists.filter(age__icontains=request.GET['filter_age'])
        if 'filter_info' in request.GET and request.GET['filter_info']:
            all_artists = all_artists.filter(information__icontains=request.GET['filter_info'])

        serializer = ArtistSerializer(all_artists, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_details(request, id):

    try:
        artist = Artist.objects.get(id= id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print(request.data)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        print(request.data)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        all_user = User.objects.all()

        if 'filter_user_name' in request.GET and request.GET['filter_user_name']:
            all_user = all_user.filter(username__icontains=request.GET['filter_user_name'])
        if 'filter_first_name' in request.GET and request.GET['filter_first_name']:
            all_user = all_user.filter(first_name__icontains=request.GET['filter_first_name'])

        serializer = UserSerializer(all_user, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ** login required **
@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        all_reviews = Review.objects.all()

        if 'filter_title' in request.GET and request.GET['filter_title']:
            all_reviews = all_reviews.filter(review_title__icontains=request.GET['filter_title'])



        serializer = ReviewSerializer(all_reviews, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ** login required **
@api_view(['GET', 'PUT', 'DELETE'])
def review_details(request, pk):

    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_user(request):
    curr_user = request.user
    # if curr_user.is_anonymous
    # userprofile = UserProfile.objects.get(user=curr_user)
    data = {
        "first_name": curr_user.first_name,
        "last_name": curr_user.last_name
    }
    return Response(data)