from savify import Savify
from savify.types import Type, Format, Quality



def download_song(url, output_path):
    s = Savify()
    url = input("Enter the URL of the song you want to download: ")
    output_path = input("Enter the path where you want to save the song: ")
    s.download(url, output_path, Type.MP3, Quality.HI_RES, Format.MP3)

