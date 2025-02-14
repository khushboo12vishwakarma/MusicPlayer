from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . views import index,get_lyrics
app_name = "App"

urlpatterns = [
    path("", index, name="index"),
    path('get-lyrics/<int:id>/', get_lyrics, name='get_lyrics'),

]










