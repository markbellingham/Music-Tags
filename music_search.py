"""Program to output tags from music files."""

import os
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
import music_tag_list_mp3 as mtl_mp3
import music_tag_list_flac as mtl_flac


def main():
    """Main controller."""
    # Specify the root directory
    path = "/home/mark/Music/"

    # List of the filetypes that are supported by the program
    # ext = ('.mp3', '.ogg', '.flac')

    '''
    Search the filesystem. For each file found, check if the extension is
    on the supported list. If it is, create a full filename including
    the path and
    '''
    for root, subdir, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root, filename)
            if filename.endswith('.mp3'):
                audio = MP3(filename)
                print(mtl_mp3.artist(audio))
                print(mtl_mp3.album_artist(audio))
                print(mtl_mp3.album(audio))
                print(mtl_mp3.trackno(audio))
                print(mtl_mp3.trackna(audio))
                print(mtl_mp3.length(audio))
                print(mtl_mp3.genre(audio))
                print(mtl_mp3.year(audio))
                print()
            elif filename.endswith('.flac'):
                audio = FLAC(filename)
                print(mtl_flac.artist(audio))
                print(mtl_flac.album_artist(audio))
                print(mtl_flac.album(audio))
                print(mtl_flac.trackno(audio))
                print(mtl_flac.trackna(audio))
                print(mtl_flac.duration(audio))
                print(mtl_flac.genre(audio))
                print(mtl_flac.year(audio))
                print()
            elif filename.endswith('.ogg'):
                audio = OggVorbis(filename)
                print(mtl_flac.artist(audio))
                print(mtl_flac.album_artist(audio))
                print(mtl_flac.album(audio))
                print(mtl_flac.trackno(audio))
                print(mtl_flac.trackna(audio))
                print(mtl_flac.duration(audio))
                print(mtl_flac.genre(audio))
                print(mtl_flac.year(audio))
                print()


main()
