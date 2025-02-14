# # Create your views here.
# from django.shortcuts import render,redirect
# from django.core.paginator import Paginator
# from . models import Song
# from django.http import JsonResponse
#
#
#
# def index(request):
#     paginator = Paginator(Song.objects.all(),1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context={"page_obj":page_obj}
#     return render(request,"main.html",context)
#
# def get_lyrics(request, song_id):
#     try:
#         song = Song.objects.get(id=song_id)
#         return JsonResponse(song.lyrics_data)
#     except Song.DoesNotExist:
#         return JsonResponse({'error': 'Song not found'}, status=404)

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Song
from django.http import JsonResponse

def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "main.html", context)

def get_lyrics(request, id):
    try:
        song = Song.objects.get(id=id)
        # Assuming song.lyrics is a string and you want to return it in a dictionary:
        return JsonResponse({'lyrics': song.lyrics})
    except Song.DoesNotExist:
        return JsonResponse({'error': 'Song not found'}, status=404)
